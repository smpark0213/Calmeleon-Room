
import RPi.GPIO as GPIO
import time
import adafruit_dht 
from board import *
import os
from datetime import datetime
 
now = datetime.now()

isBlind = False #true = Blind state // #false = no blind state

red = 13
green = 19
blue = 26
DC = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

pwmBlue = GPIO.PWM(blue, 100)
pwmRed = GPIO.PWM(red, 100)
pwmGreen = GPIO.PWM(green, 100)

pwmBlue.start(0)
pwmRed.start(0)
pwmGreen.start(0)

f = open("a.txt")

line = f.readline()
print(line)

isWlqwnd = "집중" in line 								#case1
isTodrkr = "생각" in line or "상상" in line or "아이디어" in line 			#case2
isGbtlr = "슬퍼" in line or "우울" in line or "속상해" in line				#case3
isDnsehd = "운동" in line								#case4
isDkswjd = "불안" in line or "초조" in line or "짜증" in line or "쉬고" in line		#case5
isDkarl = "암기" in line or "외우기" in line or "기억" in line 				#case6
isEkdldjxm = "식욕" in line or "다이어트" in line or "살" in line or "빠져라" in line 	#case7

if isWlqwnd:
    print("집중")
    pwmBlue.ChangeDutyCycle(100)
    pwmRed.ChangeDutyCycle(0)
    pwmGreen.ChangeDutyCycle(0)

    if now.hour >= 6 or now.hour <= 18:
        if isBlind:
            os.system("python3 blind_close.py")
            isBlind = True
    else:
        if not isBlind:
            os.system("python3 blind_open.py")
            isBline = False

    os.system("python3 case1.py")

elif isTodrkr:
    print("생각")
    pwmBlue.ChangeDutyCycle(0)
    pwmRed.ChangeDutyCycle(100)
    pwmGreen.ChangeDutyCycle(100)

    if now.hour >= 6 or now.hour <= 18:
        if isBlind:
            os.system("python3 blind_close.py")
            isBlind = True
    else:
        if not isBlind:
            os.system("python3 blind_open.py")
            isBline = False

    os.system("python3 case2.py")

elif isGbtlr:
    print("휴식")
    pwmBlue.ChangeDutyCycle(98)
    pwmRed.ChangeDutyCycle(38)
    pwmGreen.ChangeDutyCycle(86)

    if now.hour >= 6 or now.hour <= 18:
        if isBlind:
            os.system("python3 blind_close.py")
            isBlind = True
    else:
        if not isBlind:
            os.system("python3 blind_open.py")
            isBline = False

    os.system("python3 case3.py")

elif isDnsehd:
    print("운동")
    pwmBlue.ChangeDutyCycle(0)
    pwmRed.ChangeDutyCycle(100)
    pwmGreen.ChangeDutyCycle(0)

    if now.hour >= 6 or now.hour <= 18:
        if isBlind:
            os.system("python3 blind_close.py")
            isBlind = True
    else:
        if not isBlind:
            os.system("python3 blind_open.py")
            isBline = False

    os.system("python3 case4.py")

elif isDkswjd:
    print("안정")
    pwmBlue.ChangeDutyCycle(0)
    pwmRed.ChangeDutyCycle(0)
    pwmGreen.ChangeDutyCycle(100)

    if now.hour >= 6 or now.hour <= 18:
        if isBlind:
            os.system("python3 blind_close.py")
            isBlind = True
    else:
        if not isBlind:
            os.system("python3 blind_open.py")
            isBline = False

    os.system("python3 case5.py")

elif isDkarl:
    print("암기")
    pwmBlue.ChangeDutyCycle(0)
    pwmRed.ChangeDutyCycle(100)
    pwmGreen.ChangeDutyCycle(100)

    if now.hour >= 6 or now.hour <= 18:
        if isBlind:
            os.system("python3 blind_close.py")
            isBlind = True
    else:
        if not isBlind:
            os.system("python3 blind_open.py")
            isBline = False

    os.system("python3 case6.py")


elif isEkdldjxm:
    print("다이어트")
    GPIO.output(red,False)
    GPIO.output(green, False)
    GPIO.output(blue, True)

    if now.hour >= 6 or now.hour <= 18:
        if isBlind:
            os.system("python3 blind_close.py")
            isBlind = True
    else:
        if not isBlind:
            os.system("python3 blind_open.py")
            isBline = False

    os.system("python3 case7.py")




else:
    print("no no no no")







