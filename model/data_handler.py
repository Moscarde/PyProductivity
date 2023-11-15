import pandas as pd
from datetime import timedelta

class DataHandler:
    @staticmethod
    def usage_time_acum(path):
        data = pd.read_csv(path, parse_dates=["timestamp"])

        data["name"] = data["app_name"].map(lambda x: x.split(" — ")[-1].split(" - ")[-1])
        data.columns = ["timestamp", "window_title", "minutes_away", "app_name"]
        data = data.sort_values(["app_name", "timestamp"])

        data["daily_usage"] = data.apply(DataHandler.timestamps_acum, axis=1)

        data = (
            data.groupby("app_name")["daily_usage"]
            .max()
            .sort_values(ascending=False)
        )
        data = data.to_frame().reset_index()
        data['daily_usage_seconds'] = data['daily_usage'].apply(lambda x: pd.Timedelta(x).total_seconds()).astype(int)
        return data


    last_timestamp = timedelta(seconds=0)
    last_app_name = "x"
    total_delta = timedelta(seconds=0)

    @staticmethod
    def timestamps_acum(row):
        if (str(DataHandler.last_timestamp) == "0:00:00") or (row["app_name"] != DataHandler.last_app_name):
            DataHandler.last_timestamp = row["timestamp"]
            DataHandler.last_app_name = row["app_name"]
            DataHandler.total_delta = timedelta(seconds=0)
            return timedelta(seconds=0)

        elif (row["timestamp"] - DataHandler.last_timestamp) < timedelta(seconds=40):
            delta = row["timestamp"] - DataHandler.last_timestamp
            DataHandler.total_delta += delta
            return DataHandler.total_delta

        else:
            DataHandler.last_timestamp = row["timestamp"]
            return DataHandler.total_delta
