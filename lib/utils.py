import pyautogui
import time
from datetime import datetime
import subprocess
import psutil
import os
import re

def get_sub_folder_path(directory):
    entries = os.listdir(directory)

    # Filter out only the folders (directories)
    folders = {}
    for entry in entries:
        if os.path.isdir(os.path.join(directory, entry)):
            folders[entry] = os.path.join(directory, entry)

    return folders

def is_valid_regex(regex_string):
    try:
        re.compile(regex_string)
        return None
    except re.error as e:
        return e
    
def open_app(appPath):
    try:
        subprocess.Popen(appPath)
        print(f'Opened the app {appPath} at {datetime.now()}.')
    except:
        print(f'Can open the app {appPath}.')

def dont_sleep() -> None:
    pyautogui.moveTo(
        x= 1600,
        y=5,
    )
    time.sleep(5)
    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(
        x= 1600, 
        y= 7,
    )
    time.sleep(5)
    pyautogui.click()
    pyautogui.click()

def check_time(hour, minute):
    current_date = datetime.now()
    current_hour = current_date.hour
    current_minute = current_date.minute
    if current_hour == hour and current_minute == minute:
        return True
    return False

def check_if_process_running(processName):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def close_app(App_name):
    App_name_exe = str(App_name) + '.exe'
    if check_if_process_running(App_name_exe):
        os.system(f'taskkill /f /im {App_name_exe} > {os.devnull} 2>&1')
        print(f'Closed the app {App_name} at {datetime.now()}.')