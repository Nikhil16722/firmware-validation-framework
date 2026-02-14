import time
import logging
import os

# Ensure logs folder exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "device.log")

# Clear previous log file before starting fresh
if os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

# Create dedicated logger
logger = logging.getLogger("FirmwareLogger")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers if reloaded
if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


class FirmwareSimulator:

    def __init__(self):
        logger.info("Boot successful")

    def send_command(self, command):

        if command == "STATUS":
            logger.info("Status checked")
            return "Device is OK"

        elif command == "GET_TEMP":
            logger.info("Temperature read")
            return "Temperature: 35C"

        elif command == "RESET":
            logger.warning("Device reset initiated")
            return "Device Reset"

        elif command == "CRASH":
            logger.error("Memory overflow detected")
            return "System Crash"

        elif command == "DELAY":
            logger.info("Simulating delay...")
            time.sleep(3)
            return "Delayed Response"

        else:
            logger.error("Unknown command received")
            return "ERROR: Unknown Command"
