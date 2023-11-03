<p align="center">
    <a href="#"><img src="pictures/header.jpg" alt="Logo" width=80%/></a>
<p>

<center>⚠ In production ⚠</center>

>The script is an application uptime tracker that monitors active windows and records the time spent on specific applications, automatically generating daily usage reports. The script can help you analyze where you are wasting time and increase your productivity by focusing on the right applications.

## Planned Features

~~- [x] Convert old data to csv~~

~~- [x] Read data in csv~~ # Algorithm changes

- [x] Write data in csv

- [ ] Create interface with tkinter

- [ ] Manipulate data with pandas

- [ ] Create processed reports 

- [ ] Time goals with real-time visualization

- [ ] Limit app usage time by app name 

## Features 🌟

- Monitor and record the uptime of active windows.

- Detect Inactivity.

- Log Window name and timestamp in csv file. 

# Prerequisites 📋

Before using the App Uptime Tracker, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- The required Python libraries (pyautogui, pygetwindow) installed. You can install them using pip:

``` shell
pip install pyautogui pygetwindow
```

# Usage 🚀

1. Clone or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

```shell
 python pyproductivity.py
```

4. The script will start monitoring your active windows and recording their uptime.

5. You can stop the script at any time by pressing Ctrl + C in the terminal or closing it.

6. Daily usage reports are automatically generated and saved as csv files with the format "YYYY-MM-DD.csv" in the same directory as the script.

## Example Output 📊

```csv

timestamp,app_name,minutes_away
2023-11-03 16:08:04,Windows PowerShell,0
2023-11-03 16:08:08,Windows PowerShell,0
2023-11-03 16:08:08,tracker_data.py - PyWindows - Visual Studio Code,0
2023-11-03 16:08:08,Visual Studio Code,0

```

The report comprises the timestamp, window name of an application, and the duration of inactivity in minutes (which can be used for data analysis and filtering).

## Note 📝

- ⚠️ The script records the time spent on active windows. It may not capture background processes or applications that run without a visible window.
- ⚠️ Before running the script, make sure that you have set up a Python environment and installed the required libraries. 
- ⚠️ The script will create usage report files for each day in the format "YYYY-MM-DD.csv" in the logs folder. Make sure you have write permissions in that directory.
- ✔️ You can adjust the loop_interval and write_data_interval variables in the script to change the monitoring frequency and data logging.