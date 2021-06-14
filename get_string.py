##################################################################
# pip install firebase_admin
# pip install soynlp
##################################################################
## 라즈베리파이 - 파이어베이스 Real time Database - 안드로이드 APP
## DB 이용하여 라즈베리파이와 안드로이드 APP간 데이터를 주고받음
##################################################################

# 파이어베이스 - Real time database 연결
# credential과 db주소 필요
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
# 요청이 있을 시 내용을 반환하고 DB에서 삭제
def get_request(dir):
  request = dir.child('message').get()
  request_message = request['message']
  request_status = request['status']

  if request_status == 'False':
    dir.child('message').delete()
    return request_message
  else:
    return ''

# predefine_word에 공백으로 단어를 구별하여 입력
# 사용자의 요청과 predefine_word의 거리를 계산하여 가장 가까운것 반환
def check_word(request_message):
  from soynlp.hangle import levenshtein
  from soynlp.hangle import jamo_levenshtein

  best = 100
  best_index = 0
  predefine_word = '덥다 춥다 졸리다'
  predefine_word = predefine_word.split()
  input_word = request_message

  for i in range(3):
    distance = jamo_levenshtein(predefine_word[i], input_word)
    if distance < best:
      best = distance
      best_index = i

  return predefine_word[best_index]

import time
import os

dir = firebase_init()
request_message = ''

# get_request함수를 10초마다 한번씩 실행
# 공백이 반환되면 반복문의 처음으로 돌아가서 재실행
# 문자열이 반환되면 탈출

while(True):
  request_message = get_request(dir)
  time.sleep(10)

  if request_message == '':
    continue
  else:
    break;


#request_message = check_word(request_message)

print(request_message)

os.system("python3 get_string.py")
