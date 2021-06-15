from gpiozero import Motor
import time

motor = Motor(forward = 16, backward = 21)

start_time = time.time()
while(True):
    motor.backward()
    if (time.time() - start_time == 10):
        break
    else:
        continue
    
motor.backward()
time.sleep(2)

motor.stop()
time.sleep(0.5)
