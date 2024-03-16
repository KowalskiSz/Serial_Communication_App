import serial
import threading
from serial import Serial

class SerialCommunication(threading.Thread):
    def __init__(self, com, baudR):
        self.SerialObject = serial.Serial(com, baudR, timeout=0) #init the serial object

        #threading init
        threading.Thread.__init__(self)
        threading.Thread.start(self)


    def receiveData(self):
        data = self.SerialObject.read(10) #Buffer size is 10 bytes -> it can be adjustable
        if(len(data) > 0):
            try:
                intValuseofBytes = [int(x) for x in data]
                #For now debugging
                print(intValuseofBytes)
            except:
                None

    #Override run method to specify what the thread is meant to perform
    def run(self):
        while(True):
            self.receiveData()