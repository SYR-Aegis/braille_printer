import RPi.GPIO as GPIO
from ERROR import *
from time import sleep

class Solenoid():
    def __init__(self):
        self.port = 0
        self.IN = 0

    def Set_port(self, args):
        self.port = args
        GPIO.setup(self.port, GPIO.OUT)

    def Set_Input(self, args):

        self.IN = args

    def Activate(self):
        GPIO.output(self.port, bool(self.IN))
        sleep(0.1)
        GPIO.output(self.port, False)
        


