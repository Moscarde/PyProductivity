# App Uptime Tracker 📚⏰
<p align="center">
    <a href="#"><img src="pictures/header.jpg" alt="Logo" width=80%/></a>
<p>
The script is an application uptime tracker that monitors active windows and records the time spent on specific applications, automatically generating daily usage reports.

## Features 🌟

- Monitor and record the uptime of active windows.
- Calculate the time spent on specific applications.
- Automatically generate and update daily usage reports.

# Prerequisites 📋

Before using the App Uptime Tracker, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- The required Python libraries (pyautogui, pygetwindow) installed. You can install them using pip:

``` shell
pip install pyautogui pygetwindow icecream
```

# Usage 🚀

1. Clone or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

```shell
 python app_uptime_tracker.py
```

4. The script will start monitoring your active windows and recording their uptime.

5. You can stop the script at any time by pressing Ctrl + C in the terminal or closing it.

6. Daily usage reports are automatically generated and saved as text files with the format "YYYY-MM-DD.txt" in the same directory as the script.

## Example Output 📊

```txt

<~~~~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Sum ~~~~~~~~~~~~~~~~~~~~~~~~~~>
00:02:33  <~~>  Visual Studio Code
00:01:03  <~~>  Mozilla Firefox

<~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Specific ~~~~~~~~~~~~~~~~~~~~~~~~>
00:00:45  <~~>  app_uptime_tracker.py - PyWindows - Visual Studio Code
00:00:09  <~~>  AppUptimeTracker/2023-10-14.txt at main · Moscarde/AppUptimeTracker — Mozilla Firefox
00:00:54  <~~>  Moscarde/AppUptimeTracker: Application uptime tracker that monitors active windows, automatically generating daily usage reports. — Mozilla Firefox
00:01:21  <~~>  readme.md - PyWindows - Visual Studio Code
00:00:27  <~~>  2023-10-15.txt - PyWindows - Visual Studio Code

```

The report includes the total and specific usage times for individual applications.

## Note 📝

- ⚠️ The script records the time spent on active windows. It may not capture background processes or applications that run without a visible window.
- ⚠️ Before running the script, make sure that you have set up a Python environment and installed the required libraries. 
- ⚠️ The script will create usage report files for each day in the format "YYYY-MM-DD.txt" in the script's directory. Make sure you have write permissions in that directory.
- ✔️ Adjust the tick_seconds and max_inactive_time variables in the script to change the monitoring frequency and inactivity threshold.