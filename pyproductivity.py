import csv, os, time, pyautogui
import time
from datetime import datetime
import pygetwindow as gw

# new config
loop_interval = 0.1
write_data_interval = 15


def main():
    print("Starting Tracker -  Press Ctrl + C or close this window to stop tracking!")
    while True:
        try:
            windows_list = []

            for _ in range(int(write_data_interval / loop_interval)):
                active_window = gw.getActiveWindowTitle()
                if window_is_valid(active_window):
                    if not active_window in windows_list:
                        windows_list.append(active_window)

                time.sleep(loop_interval)

            write_windows_list_to_csv(windows_list)

        except Exception as e:
            print(e)


max_inactive_time = 60
inactive_time = 0
previous_mouse_pos = [0, 0]


def time_away():
    global previous_mouse_pos, inactive_time
    mouse_pos = list(pyautogui.position())

    if mouse_pos == previous_mouse_pos:
        inactive_time += write_data_interval
    else:
        previous_mouse_pos = mouse_pos
        inactive_time = 0

    return inactive_time // max_inactive_time


def window_is_valid(window):
    if window != None and window != "":
        return True


def write_windows_list_to_csv(windows_list):
    today = datetime.now()
    minutes_away = time_away()
    file_name = f"logs/{today.date()}.csv"

    if validate_file(file_name):
        print(windows_list)
        try:
            with open(file_name, mode="a", newline="", encoding="UTF-8") as csv_file:
                csv_writer = csv.writer(csv_file)

                for window in windows_list:
                    csv_writer.writerow(
                        [str(today).split(".")[0], window, minutes_away]
                    )

        except Exception as e:
            print(e)


def validate_file(file_name):
    try:
        if not os.path.exists(file_name):
            with open(file_name, mode="w", newline="", encoding="UTF-8") as file_csv:
                csv_writer = csv.writer(file_csv)
                csv_writer.writerow(["timestamp", "app_name", "minutes_away"])

        return True
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
