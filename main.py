# pylint: disable=import-error
from icecream import ic
import pygetwindow as gw
from datetime import datetime, timedelta
import os
import time
import pyautogui

# ic.disable()

sleep_loop = 9
inactivity_timer_in_seconds = 0
previous_mouse_pos = [0, 0]
inactivity = 600
line_separator = '  <~~>  '
data_separator = '<~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Specific ~~~~~~~~~~~~~~~~~~~~~~~~>'
base_doc = '''<~~~~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Sum ~~~~~~~~~~~~~~~~~~~~~~~~~~>

<~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Specific ~~~~~~~~~~~~~~~~~~~~~~~~>
'''


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
        file.write(base_doc)
        today_data = base_doc.split('\n')
        file.close()
        return today_data

    file = open(f'{date}.txt', 'r', encoding='UTF-8')
    today_data = file.read().split('\n')
    file.close()
    return today_data


def write(today, data):
    file = open(f'{today}.txt', 'w', encoding='UTF-8')
    file.write(data)
    file.close()


def add_time(window, data, full_line):
    window_line_index = data.index(full_line)

    time = full_line.split(line_separator)[0]

    time = datetime.strptime(time, '%H:%M:%S').time()
    new_time = (datetime.combine(datetime.min, time) +
                timedelta(seconds=sleep_loop)).time()
    new_time = new_time.strftime('%H:%M:%S')
    data[window_line_index] = f"{new_time}  <~~>  {window}"
    return data


def short_add_time(line):
    time, term = line.split(line_separator)
    # ic(time)
    # ic(term)
    time = datetime.strptime(time, '%H:%M:%S').time()
    new_time = (datetime.combine(datetime.min, time) +
                timedelta(seconds=sleep_loop)).time()
    new_time = new_time.strftime('%H:%M:%S')
    line = f"{new_time}{line_separator}{term}"
    return line


def get_line(term, data):
    try:
        line = list(filter(lambda line: term in line, data))[0]
        return line

    except:
        return None


def get_line_index(line, data):
    try:
        line = data.index(line)
        return line

    except:
        return None


def get_processed_data(term, data):
    # term = YouTube — Mozilla Firefox // full
    # data = stats or processed

    # get line
    # get time
    # sum time
    # replace line
    # return data

    # ic(term, data)

    old_line = get_line(term, data)  # v
    old_line_index = get_line_index(old_line, data)  # v
    # ic(old_line, old_line_index)
    # ic(term, data)

    if old_line == None:
        # Insere uma nova linha caso nao encontre
        new_line = f"00:00:0{sleep_loop}  <~~>  {term}"
        data.insert(-1, new_line)
    else:
        #substitui uma linha 
        new_line = short_add_time(old_line)  # v
        data[old_line_index] = new_line

    return data


def process_log_stats(window, full_data):
    # in
    # main.py - PyWindows - Visual Studio Code
    # # ['<~~~~~~~~~~~~stats~~~~~~~~~~~~~~>',
    #             '00:07:52  <~~>  Visual Studio Code',
    #             '00:00:20  <~~>  WakaTime — Mozilla Firefox',
    #             '00:00:35  <~~>  YouTube — Mozilla Firefox',
    #             '00:00:05  <~~>  Hearts / Wires',
    #             '<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>',
    #             '00:00:14  <~~>  main.py - PyWindows - Visual Studio Code',
    #             '00:01:33  <~~>  2023-10-15.txt - PyWindows - Visual Studio Code']

    #ic(full_data) # entrada

    # spliting datas #v
    separator_index = full_data.index(data_separator)
    data_stats = full_data[:separator_index]
    data_logs = full_data[separator_index:]
    #ic(data_stats)
    #ic(data_logs)

    # processing stats data
    window_app = window.split(' - ')[-1]

    data_stats = get_processed_data(window_app, data_stats)
    data_logs = get_processed_data(window, data_logs)

    full_data = data_stats + data_logs

    #ic(full_data)  # saida
    return full_data


def report(window):
    today = datetime.now().strftime("%Y-%m-%d")
    data = read_today_data(today)

    # testes
    ic('report', window)

    data = process_log_stats(window, data)

    data_string = '\n'.join(str(line) for line in data)
    write(today, data_string)

    # ler data - verificar se tem data da janela - somar ou adicionar uma do zero


def monitore_windows():
    repeat = True
    while repeat:

        if check_ausencia():
            active_window = gw.getActiveWindowTitle()
            if active_window != None:
                report(active_window)
            else:
                ic('None Window')
        time.sleep(sleep_loop)


if __name__ == "__main__":
    monitore_windows()
    # sum_log_stats('00:01:31  <~~>  2023-10-15.txt - PyWindows - Visual Studio Code', read_today_data(datetime.now().strftime("%Y-%m-%d")))
    # process_log_stats('2023-10-15.txt - xxxxxxx', read_today_data(datetime.now().strftime("%Y-%m-%d")))
    



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
