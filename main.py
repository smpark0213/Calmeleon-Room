
import RPi.GPIO as GPIO
import time
import adafruit_dht 
from board import *
import os
from datetime import datetime
 
now = datetime.now()

def firebase_init():
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

    credential = credentials.Certificate('sensorandnetwork-firebase-adminsdk-iy4wj-3e52cbe6c1.json')
    firebase_admin.initialize_app(credential, {'databaseURL' : 'https://sensorandnetwork-default-rtdb.firebaseio.com/'})
    dir = db.reference()

    return dir

# DB에서 사용자의 요청을 읽어옴
# 아무 요청이 없을 시 비어잇는 문자열 반환
# status가 false일시 메세지 반환
def get_request(dir):
    request = dir.child('message').get()
    request_message = request['message']
    request_status = request['status']

    if request_status == 'False':
      return request_message
    else:
      return 'Yet'
# record에 날짜, 메시지, 안밖 온도 저장
def save_record(dir, request_message, color, temp_in, temp_out):
    from datetime import datetime

    record_ref = dir.child('record')

    date = datetime.today().strftime('%Y%m%d%H%M')

    record = record_ref.push({'date' : date,
                            'message' : request_message,
                            'temperature_inside' : temp_in,
                            'temperature_outside' : temp_out})
  
    decorate_ref = dir.child('Decorate')

    date = datetime.today().strftime('%Y%m%d')
    decorate = decorate_ref.push({'color' : color,
                                'date' : date})


dir = firebase_init()


  # get_request함수를 10초마다 한번씩 실행
  # 공백이 반환되면 반복문의 처음으로 돌아가서 재실행
  # 문자열이 반환되면 탈출
while(True):
    request_message = ''
    print("readread")
    request_message = get_request(dir)
    time.sleep(3)

    if request_message == 'Yet':
        continue
    else:
        dir.child('message').set({'message' : request_message, 'status' : 'True'})
        break

print(request_message)
  
  # 파일에 메시지 저장
f = open("a.txt", mode = 'wt', encoding = 'utf-8')
f.write(request_message)
f.close()

  #save_record(dir, request_message, 'blue', '15', '20')


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
#f.write("")

print(line)

isWlqwnd = "집중" in line	 							#case1
isTodrkr = "생각" in line or "상상" in line or "아이디어" in line 			#case2
isGbtlr = "슬퍼" in line or "우울" in line or "속상해" in line				#case3
isDnsehd = "운동" in line 								#case4
isDkswjd = "불안" in line or "초조" in line or "짜증" in line or "쉬고" in line		#case5
isDkarl = "암기" in line or "외우기" in line or "기억" in line 				#case6
isEkdldjxm = "식욕" in line or "다이어트" in line or "빠져라" in line		 	#case7

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






