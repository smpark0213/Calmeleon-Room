from gpiozero import Motor
import time

motor = Motor(forward = 16, backward = 21)

motor.backward()
time.sleep(2)

motor.stop()
time.sleep(0.5)
