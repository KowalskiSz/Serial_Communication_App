import SerialCom
from serial.tools import list_ports

if __name__ == '__main__':
    sCom = SerialCom.SerialCommunication('COM1', 9600)

