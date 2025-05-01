import os
import winreg
import psutil

# Base paths
APPDATA     = os.getenv("APPDATA")                 
USERPROFILE = os.getenv("USERPROFILE")             

# The stealth copy your virus creates in APPDATA
PERSIST_EXE = os.path.join(APPDATA, "WindowsExplorer.exe")

# All filenames used when spreading into user folders
SPREAD_NAMES = [
    "ReportGenerator.exe","Invoice_MAY2025.scr","SystemUpdate.com","PhotoViewer.exe",
    "UserManual.scr","Setup_Files.exe","TaskScheduler.com","SecurityPatch.scr",
    "DownloadManager.exe","MusicPlayer.scr","GameLauncher.com","AppInstaller.exe",
    "DesktopCleaner.scr","NewVersion.exe","BackupTool.com","ImageEditor.scr",
    "FileOrganizer.exe","SoftwareUpdate.scr","ZipExtractor.com","DocumentViewer.exe"
]

def remove_persistence():
    #1. Delete the hidden executable from %APPDATA%
    #2. Remove the Registry Run entry under HKCU\...\Run

    # 1. Remove the hidden copy
    if os.path.exists(PERSIST_EXE):
        try:
            os.remove(PERSIST_EXE)
        except Exception:
            return False

    # 2. Remove the auto-start registry value
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
            0, winreg.KEY_SET_VALUE
        )
        winreg.DeleteValue(key, "Windows Explorer")
        winreg.CloseKey(key)
    except Exception:
        # if the key/value doesn’t exist or fails, we ignore
        pass

    return True

def remove_spread():
    #Delete any spread copies:
    success = True

    # A) Clean user folders
    for folder in ("Downloads", "Desktop", "Documents"):
        folder_path = os.path.join(USERPROFILE, folder)
        for name in SPREAD_NAMES:
            file_path = os.path.join(folder_path, name)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception:
                    success = False

    # B) Clean removable drives
    for part in psutil.disk_partitions():
        if 'removable' in part.opts:
            usb_path = os.path.join(part.mountpoint, "WindowsExplorer.exe")
            if os.path.exists(usb_path):
                try:
                    os.remove(usb_path)
                except Exception:
                    success = False

    return success

def main():
    """Run both cleanup routines and print a single summary line."""
    p_ok = remove_persistence()
    s_ok = remove_spread()

    if p_ok and s_ok:
        print("Kill switch completed successfully.")
    else:
        print("Kill switch completed with some errors.")

if __name__ == "__main__":
    main()
