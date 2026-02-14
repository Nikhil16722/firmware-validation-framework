import time
from device.firmware_simulator import FirmwareSimulator
from utils.log_validator import check_log_for_error, count_log_keyword

LOG_FILE = "logs/device.log"

def test_device_boot():
    device = FirmwareSimulator()
    assert device is not None

def test_crash_detection():
    device = FirmwareSimulator()
    device.send_command("CRASH")
    time.sleep(1)
    assert check_log_for_error(LOG_FILE) is True

def test_reset_logged():
    device = FirmwareSimulator()
    device.send_command("RESET")
    time.sleep(1)
    warning_count = count_log_keyword(LOG_FILE, "WARNING")
    assert warning_count >= 1
