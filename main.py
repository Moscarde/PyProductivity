# pylint: disable=import-error
from icecream import ic
import pygetwindow as gw
from datetime import datetime, timedelta
import os
import time
import pyautogui

# ic.disable()

sleep_loop = 5
inactivity_timer_in_seconds = 0
previous_mouse_pos = [0, 0]
inactivity = 60

def check_ausencia():
    global previous_mouse_pos, inactivity_timer_in_seconds
    mouse_pos = list(pyautogui.position())

    if mouse_pos == previous_mouse_pos:
        if inactivity_timer_in_seconds > inactivity:
            print('inative')
            return False
        else:
            inactivity_timer_in_seconds += sleep_loop
            return True
    else:
        previous_mouse_pos = mouse_pos
        inactivity_timer_in_seconds = 0
        return True


def read_today_data(date):
    if not os.path.exists(f'{date}.txt'):
        file = open(f'{date}.txt', 'w')
        file.close()
        return []

    file = open(f'{date}.txt', 'r')
    today_data = file.read().split('\n')
    file.close()
    return today_data

def write(today, data):
    # today_data = read_today(today)

    # today_data[1] = calc_elapsed_time(today_data[1], study_duration)
    # today_data.append(
    #     f"Date {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} - Time Spent {round_delta(study_duration)}")

    # today_data_string = '\n'.join(str(line) for line in today_data)

    file = open(f'{today}.txt', 'w')
    file.write(data)
    file.close()

def add_time(window, data, full_line):
    window_line_index = data.index(full_line)

    time = full_line.split('  <~~>  ')[0]

    time = datetime.strptime(time, '%H:%M:%S').time()
    new_time = (datetime.combine(datetime.min, time) + timedelta(seconds=5)).time()
    new_time = new_time.strftime('%H:%M:%S')
    data[window_line_index] = f'{new_time}  <~~>  {window}'
    return data
    

def report(window):
    today = datetime.now().strftime("%Y-%m-%d")
    data = read_today_data(today)

    #testes
    ic('report', window)

    
    full_line = list(filter(lambda line: window in line, data))

    if len(full_line) == 0:
        window = f"00:00:05  <~~>  {window}"
        data.append(window)
    else:
        full_line= full_line[0]
        data = add_time(window, data, full_line)

    data_string = '\n'.join(str(line) for line in data)
    write(today, data_string)

    
    # ler data - verificar se tem data da janela - somar ou adicionar uma do zero


def monitore_windows():
    repeat = True
    while repeat:
        if check_ausencia():
            active_window = gw.getActiveWindowTitle()
            report(active_window)
        time.sleep(sleep_loop)


if __name__ == "__main__":
    monitore_windows()
    #report('main.py- lll - PyWindows - Visual Studio Code')
    


# CC ============================================
def read_today(today):
    if not os.path.exists(f'{today}.txt'):
        file = open(f'{today}.txt', 'w')
        file.close()
        return ['TOTAL_TIME:', '0:00:00', 'LOG:']

    file = open(f'{today}.txt', 'r')
    study_duration = file.read().split('\n')
    file.close()
    return study_duration


def calc_elapsed_time(stored, studied):
    elapsed_time = datetime.strptime(stored, "%H:%M:%S") + studied
    elapsed_time = elapsed_time.strftime("%H:%M:%S")
    return elapsed_time


def write_today(today, study_duration):
    today_data = read_today(today)

    today_data[1] = calc_elapsed_time(today_data[1], study_duration)
    today_data.append(
        f"Date {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} - Time Spent {round_delta(study_duration)}")

    today_data_string = '\n'.join(str(line) for line in today_data)

    file = open(f'{today}.txt', 'w')
    file.write(today_data_string)
    file.close()


def round_delta(x): return str(x).split('.')[0]
