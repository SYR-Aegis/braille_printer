import RPi.GPIO as GPIO
from ERROR import *
from time import sleep
import sys

'''
code reference by
https://cafe.naver.com/mechawiki/30
'''

GPIO.setmode(GPIO.BCM)

class Motor:
    def __init__(self):
        self.IN=[]
        self.speed=20
        self.count=0
        # self.countsperrev=512
        self.seq = [[1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]]
        self.stepcount = 8
        self.dir = 0
        self.waittime = self.speed/float(20000)
        self.step_counter = 0
        self.step_dir = 0


    def Set_Input(self,*args):
        if(len(args) != 4):
            raise IN_LENGTH_ERROR
        else:
            self.IN = [port for port in args]

        for pin in self.IN:
            print("setting pins....")
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    def Clockwise(self):
        # for i in range(8):
        #     print(6-i)
        #     self.Set_Output(6-i)
        #     sleep(self.speed/1000)

        self.step_dir = 1

        for pin in range(0,4):
            xpin = self.IN[pin]
            if self.seq[self.step_counter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        self.step_counter += self.step_dir

        if self.step_counter >= self.stepcount:
            self.step_counter = 0
        if self.step_counter < 0:
            self.step_counter = self.stepcount + self.step_dir

        sleep(self.waittime)

    def Counter_Clockwise(self):
        # for i in range(8):
        #     self.Set_Output(i)
        #     sleep(self.speed/1000)

        self.step_dir = -1

        for pin in range(0, 4):
            xpin = self.IN[pin]
            if self.seq[self.step_counter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        self.step_counter += self.step_dir

        if self.step_counter >= self.stepcount:
            self.step_counter = 0
        if self.step_counter < 0:
            self.step_counter = self.stepcount + self.step_dir

        sleep(self.waittime)

    def Set_Output(self,out):
        for i, port in zip(range(4), self.IN):
            #GPIO.output(port,bool(Bit_Read(self.lookup[out],i)))
            print(port,bool(Bit_Read(self.lookup[out],i)))

def Bit_Read(object:str, n:int)->int:

    return int(object[-(n+1)])


