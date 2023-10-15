import os
import time
from datetime import datetime, timedelta

import pyautogui
import pygetwindow as gw
from icecream import ic

tick_seconds = 9  # max 9
inactive_time = 0
max_inactive_time = 600
previous_mouse_pos = [0, 0]

line_separator = "  <~~>  "
data_separator = (
    "<~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Specific ~~~~~~~~~~~~~~~~~~~~~~~~>"
)
base_data = """<~~~~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Sum ~~~~~~~~~~~~~~~~~~~~~~~~~~>

<~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Specific ~~~~~~~~~~~~~~~~~~~~~~~~>
"""


def is_active():
    global previous_mouse_pos, inactive_time
    mouse_pos = list(pyautogui.position())

    if mouse_pos == previous_mouse_pos:
        if inactive_time > max_inactive_time:
            print("inative")
            return False
        else:
            inactive_time += tick_seconds
            return True
    else:
        previous_mouse_pos = mouse_pos
        inactive_time = 0
        return True


def read_data(date):
    if not os.path.exists(f"{date}.txt"):
        file = open(f"{date}.txt", "w")
        file.write(base_data)
        data = base_data.split("\n")
        file.close()
        return data

    else:
        file = open(f"{date}.txt", "r", encoding="UTF-8")
        data = file.read().split("\n")
        file.close()
        return data


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
        new_line = f"00:00:0{tick_seconds}  <~~>  {window_title}"
        data.insert(-1, new_line)
    else:
        # Substitui uma linha
        new_line = add_time(old_line)
        data[old_line_index] = new_line

    return data


def process_report(window, full_data):
    # spliting datas
    separator_index = full_data.index(data_separator)
    data_stats = full_data[:separator_index]
    data_logs = full_data[separator_index:]

    # processing data
    data_logs = get_processed_data(window, data_logs)
    window_app = window.split(" - ")[-1]
    data_stats = get_processed_data(window_app, data_stats)

    full_data = data_stats + data_logs

    return full_data


def report(window):
    todays_date = datetime.now().strftime("%Y-%m-%d")
    data = read_data(todays_date)
    
    # console log
    ic("report", window)
    data = process_report(window, data)

    data_string = "\n".join(str(line) for line in data)
    write_data(todays_date, data_string)


def main():
    repeat = True
    while repeat:

        if is_active():
            active_window = gw.getActiveWindowTitle()
            if active_window != None:
                report(active_window)

        time.sleep(tick_seconds)


if __name__ == "__main__":
    main()