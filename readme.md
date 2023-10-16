# App Uptime Tracker 📚⏰

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

5. You can stop the script at any time by pressing Ctrl + C in the terminal.

6. Daily usage reports are automatically generated and saved as text files with the format "YYYY-MM-DD.txt" in the same directory as the script.

## Example Output 📊

Here is an example of the generated usage report file (e.g., "2023-10-15.txt"):

```txt

<~~~~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Sum ~~~~~~~~~~~~~~~~~~~~~~~~~~>
00:22:39  <~~>  Visual Studio Code

<~~~~~~~~~~~~~~~~~~~~~~~~ Usage time - Specific ~~~~~~~~~~~~~~~~~~~~~~~~>
00:22:14  <~~>  main.py - PyWindows - Visual Studio Code
00:00:25  <~~>  2023-10-15.txt - PyWindows - Visual Studio Code

```

The report includes the total and specific usage times for individual applications.

## Note 📝

- ⚠️ The script records the time spent on active windows. It may not capture background processes or applications that run without a visible window.
- ⚠️ Before running the script, make sure that you have set up a Python environment and installed the required libraries. 
- ⚠️ The script will create usage report files for each day in the format "YYYY-MM-DD.txt" in the script's directory. Make sure you have write permissions in that directory.
- ✔️ Adjust the tick_seconds and max_inactive_time variables in the script to change the monitoring frequency and inactivity threshold.