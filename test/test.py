import os
import time

pid = os.fork()

if pid > 0:
    # Parent Process
    time.sleep(60)
else if pid == 0:
    # Child Process
    print("Zombie Process Created Successfully!")
    os._exit(0)
else:
    # Child Process creation failed
    print("Sorry! Child Process cannot be created...")
