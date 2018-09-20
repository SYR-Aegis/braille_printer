import RPi.GPIO as GPIO
from ERROR import *

#17

class Solenoid():
    def __init__(self):
        self.State = [0,0,0]
        self.IN = []

    def Set_State(self, *args):
        if len(args) != 3:
            raise PARAMETER_LENGTH_ERROR
        else:
            for argument in args:
                if argument != 1 or argument != 0:
                    raise SOLENOID_STATE_ERROR
                else:
                    pass

            self.State = [x for x in args]

    def Set_Input(self, args):

        self.IN = args

    def Setup(self):
        for port in self.IN:
            GPIO.setup(port, GPIO.OUT)

    def Activate(self):
        for port, state in self.IN, self.State:
            GPIO.output(port, bool(state))