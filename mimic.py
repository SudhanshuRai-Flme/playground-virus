import os
import time
def mimic():
    try:
        os.system("cls" if os.name == "nt" else "clear")
        print("Window Explorer debugging ........")
        time.sleep(2)
    except Exception as e:
        print("Unexpected error please run the program again")