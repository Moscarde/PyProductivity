import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("logs/2023-11-06.csv", parse_dates=["timestamp"])

data["name"] = data["app_name"].map(lambda x: x.split(" — ")[-1].split(" - ")[-1])
data.columns = ["timestamp", "window_title", "minutes_away", "app_name"]
data = data.sort_values(["app_name", "timestamp"])

total_usage = data.copy()
last_timestamp = timedelta(seconds=0)
last_app_name = "x"
total_delta = timedelta(seconds=0)


def sum_times(row):
    global last_timestamp, last_app_name, total_delta
    if (str(last_timestamp) == "0:00:00") or (row["app_name"] != last_app_name):
        last_timestamp = row["timestamp"]
        last_app_name = row["app_name"]
        total_delta = timedelta(seconds=0)
        return timedelta(seconds=0)

    elif (row["timestamp"] - last_timestamp) < timedelta(seconds=40):
        delta = row["timestamp"] - last_timestamp
        total_delta += delta
        return total_delta

    else:
        last_timestamp = row["timestamp"]
        return total_delta


total_usage["daily_usage"] = data.apply(sum_times, axis=1)


total_usage = (
    total_usage.groupby("app_name")["daily_usage"].max().sort_values(ascending=False)
)

total_usage = total_usage.head(5).to_frame()
total_usage['daily_usage'] = (total_usage['daily_usage'] / np.timedelta64(1, 'h'))

values_to_plot = total_usage.values[:, 0]

fig, ax = plt.subplots()
ax.bar(total_usage.index, values_to_plot)

plt.show()