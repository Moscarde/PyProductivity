import json
import os
import time
from datetime import datetime, timedelta

import pyautogui
import pygetwindow as gw
from icecream import ic
import pandas as pd

# load from config.json
tick_seconds = 9
max_inactive_time = 600
console_log = 1

inactive_time = 0
previous_mouse_pos = [0, 0]

line_separator = "  <~~>  "
data_separator = (
    "<~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Specific ~~~~~~~~~~~~~~~~~~~~~~~~>"
)
base_data = """<~~~~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Sum ~~~~~~~~~~~~~~~~~~~~~~~~~~>

<~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Specific ~~~~~~~~~~~~~~~~~~~~~~~~>
"""


def load_configs():
    print('Loading configs...')
    global tick_seconds, max_inactive_time, console_log

    try:
        with open("config.json") as f:
            config = json.load(f)

        tick_seconds = int(config["tick_seconds"])
        ic(tick_seconds)
        max_inactive_time = int(config["max_inactive_time"])
        ic(max_inactive_time)

        if int(config["console_log"]) == 0:
            ic.disable()
        ic(console_log)

    except FileNotFoundError as e:
        print(f"config.json not found!\n{e}")
        print("Loading default configs...")
    except KeyError as e:
        print(f"Error in config.json key!\n{e}")
        print("Loading default configs...")
    except Exception as e:
        print(e)
        print("Loading default configs...")


def is_active():
    global previous_mouse_pos, inactive_time
    mouse_pos = list(pyautogui.position())

    if mouse_pos == previous_mouse_pos:
        if inactive_time > max_inactive_time:
            inactive_time += tick_seconds
            ic(inactive_time)
            return False
        else:
            inactive_time += tick_seconds
            return True
    else:
        previous_mouse_pos = mouse_pos
        inactive_time = 0
        return True


def read_data(date):
    if not os.path.exists(f"{date}.csv"):
        file = open(f"{date}.csv", "w")
        file.close()
        # retornar data
        return ''
    
    else:
        try:
            df = pd.read_csv(f'{date}.csv')
            return df
        except:
            return "Sem daata"
            


def write_data(date, data):
    file = open(f"{date}.txt", "w", encoding="UTF-8")
    file.write(data)
    file.close()


def add_time(line):
    timestamp, window_title = line.split(line_separator)

    timestamp = datetime.strptime(timestamp, "%H:%M:%S").time()
    converted_timestamp = datetime.combine(datetime.min, timestamp)

    new_timestamp = (converted_timestamp + timedelta(seconds=tick_seconds)).time()
    new_timestamp = new_timestamp.strftime("%H:%M:%S")
    line = f"{new_timestamp}{line_separator}{window_title}"
    return line


def get_line(window_title, data):
    try:
        line = list(filter(lambda line: window_title in line, data))[0]
        index = data.index(line)
        return line, index

    except:
        return None, None


def get_processed_data(window_title, data):
    old_line, old_line_index = get_line(window_title, data)

    if old_line == None:
        # Insere uma nova linha caso nao encontre
        new_line = f"00:00:00  <~~>  {window_title}"
        data.insert(-1, new_line)
    else:
        # Substitui uma linha
        new_line = add_time(old_line)
        data[old_line_index] = new_line

    return data


def get_app_name(window_title):
    window_app_name = window_title.split(" - ")[-1]
    window_app_name = window_app_name.split(" — ")[-1]
    return window_app_name


def process_report(window_title, full_data):
    # spliting datas
    separator_index = full_data.index(data_separator)
    data_stats = full_data[:separator_index]
    data_logs = full_data[separator_index:]

    # processing data
    data_logs = get_processed_data(window_title, data_logs)
    window_app_name = get_app_name(window_title)
    data_stats = get_processed_data(window_app_name, data_stats)

    full_data = data_stats + data_logs

    return full_data


def report(window):
    todays_date = datetime.now().strftime("%Y-%m-%d")
    data = read_data(todays_date)

    data = process_report(window, data)

    data_string = "\n".join(str(line) for line in data)
    write_data(todays_date, data_string)


def main():
    load_configs()

    print('Starting Tracker -  Press Ctrl + C or close this window to stop tracking!')
    while True:
        if is_active():
            active_window = gw.getActiveWindowTitle()
            if active_window != None and active_window != "":
                ic("report", active_window)  # console_log
                report(active_window)

        time.sleep(tick_seconds)


if __name__ == "__main__":
    #main()
    todays_date = datetime.now().strftime("%Y-%m-%d")
    print(read_data(todays_date))
