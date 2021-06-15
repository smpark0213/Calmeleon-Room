## 라즈베리파이 - 파이어베이스 Real time Database - 안드로이드 APP
## DB 이용하여 라즈베리파이와 안드로이드 APP간 데이터를 주고받음

# 파이어베이스 - Real time database 연결
# credential과 db주소 필요
def firebase_init():
  import firebase_admin
  from firebase_admin import credentials
  from firebase_admin import db

  credential = credentials.Certificate('/content/sensorandnetwork-firebase-adminsdk-iy4wj-3e52cbe6c1.json')
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

# record에 날짜, 메시지, 안밖 온도 저장
# decorate에 날짜, color 저장
def save_record(dir, request_message, color, temp_in, temp_out):
  from datetime import datetime

  record_ref = dir.child('record')

  date = datetime.today().strftime('%Y%m%d%H%M')

  record = record_ref.push({'date' : date,
                            'message' : request_message,
                            'temperature_inside' : temp_in,
                            'temperature_outside' : temp_out})
  
  decorate_ref = dir.child('Decorate')

  decorate = decorate_ref.push({'color : ' color,
                                'date : ', date})

# 메인
if __name__ == '__main__':
  import time

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
      dir.child('message').set({'message' : request_message, 'status' : 'True'})
      break

  request_message = check_word(request_message)

  print(request_message)

  save_record(dir, request_message,, 'red' '15', '20')