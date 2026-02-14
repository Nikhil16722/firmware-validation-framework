from device.firmware_simulator import FirmwareSimulator

def test_status_command():
    device = FirmwareSimulator()
    response = device.send_command("STATUS")
    assert response == "Device is OK"

def test_get_temp_command():
    device = FirmwareSimulator()
    response = device.send_command("GET_TEMP")
    assert "Temperature" in response

def test_invalid_command():
    device = FirmwareSimulator()
    response = device.send_command("INVALID")
    assert "ERROR" in response
