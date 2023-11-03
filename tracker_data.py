import json
import os
import time
from datetime import datetime, timedelta
import csv

import pyautogui
import pygetwindow as gw
from icecream import ic
import pandas as pd

# new config
loop_interval = 0.5
write_data_interval = 5

# load from config.json







def main():
    # load_configs()
    print("Starting Tracker -  Press Ctrl + C or close this window to stop tracking!")
    while True:
        try:
            windows_list = []

            for _ in range(int(write_data_interval / loop_interval)):
                active_window = gw.getActiveWindowTitle()
                if user_is_active() and validate_window(active_window):
                    if not active_window in windows_list:
                        windows_list.append(active_window)

                time.sleep(loop_interval)

            write_windows_list_to_csv(windows_list)

        except Exception as e:
            print(e)

max_inactive_time = 15
inactive_time = 0
previous_mouse_pos = [0, 0]

def user_is_active():
    global previous_mouse_pos, inactive_time
    mouse_pos = list(pyautogui.position())

    if mouse_pos == previous_mouse_pos:
        if inactive_time > max_inactive_time:
            print('Inactive time:', inactive_time)
            inactive_time += loop_interval
            return False
        
        inactive_time += loop_interval
        return True
    else:
        previous_mouse_pos = mouse_pos
        inactive_time = 0
        return True


def validate_window(window):
    if window != None and window != "":
        return True


def write_windows_list_to_csv(windows_list):
    today = datetime.now()
    file_name = f"{today.date()}.csv"

    if validate_file(file_name):
        try:
            with open(file_name, mode="a", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)

                for window in windows_list:
                    csv_writer.writerow([str(today).split(".")[0], window])

        except Exception as e:
            print(e)


def validate_file(file_name):
    try:
        if not os.path.exists(file_name):
            with open(file_name, mode="w", newline="") as file_csv:
                csv_writer = csv.writer(file_csv)
                # Escreva a nova linha no arquivo CSV
                csv_writer.writerow(["total_time", "app_name"])

        return True
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
