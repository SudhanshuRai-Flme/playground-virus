import threading
def cpu_stress():
    try:
        def stress_cpu():
            while True:
                num = 2
                while True:
                    for i in range(2, num):
                        if num % i == 0:
                            break
                    else:
                        pass
                    num += 1
        # Create multiple threads to stress multiple CPU cores
        threads = []
        for _ in range(4):  # _ is just a placeholder variable as we don't intend to break this loop and the 4 is the number of threads we want to create
            t = threading.Thread(target=stress_cpu)
            threads.append(t)
            t.start()

        # Wait for all threads to finish (but the thing is they will never finish so we will see as their CPU burns itself out)
        for t in threads:
            t.join()
    
    except Exception as e:
        print(f"Error in CPU stress: {e}")
