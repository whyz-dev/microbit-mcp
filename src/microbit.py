import serial
import serial.tools.list_ports

class Microbit:
    def __init__(self):
        self.port = self.find_microbit()
        self.ser = serial.Serial(self.port, 115200, timeout=1)

    def __del__(self):
        self.ser.close() 

    # micro:bit 찾기
    def find_microbit(self):
        for port in serial.tools.list_ports.comports():
            if "micro:bit" in port.description or "0D28" in port.hwid:
                return port.device
        return None

    def send_message(self, message):
        self.ser.write((message + '\n').encode())

    def read_message(self):
        return self.ser.readline().decode().strip()