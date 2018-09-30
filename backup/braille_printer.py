#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from solenoid import *
from motor import *
from last_modified import *

class braille_printer():
    def __init__(self):

        self.motorpin1 = [6,13,19,26]
        self.motorpin2 = [2,3,4,17]
        self.motorpin3 = [14,15,18,23]

        self.solpin1 = 21
        self.solpin2 = 20
        self.solpin3 = 16
        
        self.M1 = Motor()
        self.M2 = Motor()
        self.M3 = Motor()

        self.sol1 = Solenoid()
        self.sol2 = Solenoid()
        self.sol3 = Solenoid()

        self.filename = "test.txt"

        self.full_text = change_lab(self.filename)
        self.splited_text = []
        self.brailled_text = []

        self.word_len = 20
        self.dir = True

    def setup(self):
        self.sol1.Set_port(self.solpin1)
        self.sol2.Set_port(self.solpin2)
        self.sol3.Set_port(self.solpin3)
        
        self.M1.Set_Input(*self.motorpin1)
        self.M2.Set_Input(*self.motorpin2)
        self.M3.Set_Input(*self.motorpin3)
        
    def text_split(self):

        cnt = 0
        loop = True
        line_dir = True

        while loop:
            tmp = []
            
            for i in range(self.word_len):
                
                if i+cnt >= len(self.full_text):
                    loop = False
                else:
                    tmp.append(self.full_text[i+cnt])
            
            if line_dir:
                self.splited_text.append(tmp)
                line_dir = not line_dir
            else:
                tmp.reverse()
                self.splited_text.append(tmp)
                line_dir = not line_dir
            cnt += 20

    def make_braille(self):
        for line, line_num  in zip(self.splited_text, range(len(self.splited_text))):
            tmp = []
            if line_num % 2 == 0:
                for word in line:
                    b_tmp = []
                
                    braille = bin(word)[2:]
                
                    if len(braille) < 6:
                        fake_str = ""
                        for i in range(6 - len(braille)):
                            fake_str += "0"
                        braille = fake_str + braille

                    b_tmp.append(braille[:3])
                    b_tmp.append(braille[3:])
                    tmp.append(b_tmp)
            else:
                for word in line:
                    b_tmp = []
                    braille = bin(word)[2:]

                    if len(braille) < 6:
                        fake_str = ""
                        for i in range(6 - len(braille)):
                            fake_str += "0"
                        braille = fake_str + braille

                    b_tmp.append(braille[3:])
                    b_tmp.append(braille[:3])
                    tmp.append(b_tmp)

            self.brailled_text.append(tmp)
    
    def push_sol(self, braille):
        print(braille)
        self.sol1.Set_Input(int(braille[0]))
        self.sol2.Set_Input(int(braille[1]))
        self.sol3.Set_Input(int(braille[2]))

        self.sol1.Activate()
        self.sol2.Activate()
        self.sol3.Activate()

        print("pushing solenoid")

    def move_motor_col(self):
        if self.dir:
            for i in range(2547):
                self.M1.Clockwise()
                print("moving col")
        else:
            for i in range(2547):
                self.M1.Counter_Clockwise()
                print("moving col")

    def move_motor_word(self):
        if self.dir:
            for i in range(2038):
                self.M1.Clockwise()
                print("moving word")
        else:
            for i in range(2038):
                self.M1.Counter_Clockwise()
                print("moving word")

    def move_motor_line(self):
        for i in range(10190):
            self.M2.Clockwise()
            self.M3.Counter_Clockwise()
            print("moving line")
    
    def print_braille(self):

        for line in self.brailled_text:
            for word in line:
                for col in word:
                    self.push_sol(col)
                    self.move_motor_col()
                self.move_motor_word()
            self.dir = not self.dir
            self.move_motor_word()
            self.move_motor_line()
                    
        
b = braille_printer()
b.setup()
print("done")
b.text_split()
print(b.splited_text)
b.make_braille()
print(b.brailled_text)
b.print_braille()

