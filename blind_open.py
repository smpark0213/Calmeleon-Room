from gpiozero import Motor
import time

motor = Motor(forward = 16, backward = 21)


motor.forward()
time.sleep(2)

motor.stop()
time.sleep(0.5)
