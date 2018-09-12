#import RPi.GPIO as GPIO
from ERROR import *
from time import sleep

'''
code reference by
https://cafe.naver.com/mechawiki/30
'''

GPIO.setmode(GPIO.BCM)

class Motor:
    def __init__(self):
        self.IN=[]
        self.speed=0
        self.count=0
        self.countsperrev=512
        self.lookup = ['0b01000','0b01100','0b00100','0b00110','0b00010','0b00011','0b01001']

    def Set_Input(self,*args):
        if(len(args) != 4):
            raise IN_LENGTH_ERROR
        else:
            self.IN = [port for port in args]

    def Setup(self):
        for port in self.IN:
            GPIO.setup(port, GPIO.OUT)

    def Clockwise(self):
        for i in range(8):
            self.Set_Output(7-i)
            sleep(self.speed/1000)

    def Counter_Clockwise(self):
        for i in range(8):
            self.Set_Output(i)
            sleep(self.speed/1000)

    def Set_Output(self,out):
        for i, port in range(4), self.IN:
            GPIO.output(port,bool(Bit_Read(self.lookup[out],i)))

def Bit_Read(object:str, n:int)->int:
    return int(object[-(n+1)])
