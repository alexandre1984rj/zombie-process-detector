import psutil
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler('/var/log/zombie-process-detector.log')
                    ])

def check_for_zombies():

    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            if proc.status() == psutil.STATUS_ZOMBIE:
                
                pInfoDict = proc.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent'])
                container_id = None

                process = psutil.Process(proc.pid)
                ppid = process.ppid()

                logging.debug(f"Checking for zombie processes on pid {proc.pid}")

                with open(f"/proc/{ppid}/cgroup", "rt") as f:
                    for line in f.readlines():
                        if "docker" in line or "kubepods" in line:
                            container_id = line.split("/")[-1].strip()[:12]
                            break

                logging.warning(f"Zombie process found on pid {proc.pid} (process name: {proc.name()} - pid in parent: {ppid} - container id: {container_id})")

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

if __name__ == '__main__':
    logging.info("Starting my app")
    try:
        while True:
            check_for_zombies()
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("Stopping my app")
