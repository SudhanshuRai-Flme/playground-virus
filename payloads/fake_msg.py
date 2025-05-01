import psutil
import ctypes
import time

# List of applications to monitor (including File Explorer)
target_apps = ["chrome.exe", "firefox.exe", "brave.exe", "explorer.exe"]

def show_fake_message():
    try:
        ctypes.windll.user32.MessageBoxW(0, "Well my friend it seems like the playground of your system has been tainted and the time has come to fix it.\nThis will be a good learning experience I hope.", "System Alert", 0x30)
        #any message can be added to the above line to change the message in the pop up box
        # 0x30 is the icon type (exclamation icon)
    except Exception as e:
        print(f"Error displaying fake message: {e}")

def monitor_apps():
    try:
        while True:
            for proc in psutil.process_iter(['pid', 'name']):
                # Check if the process name is in our list of target apps
                if proc.info['name'].lower() in target_apps:
                    show_fake_message()
                    time.sleep(2)  # Wait for a while to avoid spamming the message
            time.sleep(1)  # Check every second for new processes
    except KeyboardInterrupt:
        print("Monitoring stopped.")
