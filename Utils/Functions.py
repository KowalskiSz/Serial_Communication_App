from serial.tools import list_ports
import typing

def GetCOMPorts() -> list:
    listOfPorts = list_ports.comports()
    com = list()

    for p in listOfPorts:
        #print(str(p.name))
        com.append(p.name)
    return com