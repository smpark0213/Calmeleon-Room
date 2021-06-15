import os
import threading
import adafruit_dht
from board import *
from time import sleep

SENSOR_PIN_IN = D17
SENSOR_PIN_OUT = D27

dht22_in = adafruit_dht.DHT22(SENSOR_PIN_IN, use_pulseio=False)
dht22_out = adafruit_dht.DHT22(SENSOR_PIN_OUT, use_pulseio=False)


def mp3():
    os.system("mpg321 exercise.mp3")
    
def getValue():
    os.system("python3 main.py")
 

def temper():
    temp = True
    while True:
        try:
            temperature_inside = dht22_in.temperature
            temperature_outside = dht22_out.temperature
            print(f"Outside Temperature= {temperature_outside:.1f}°C")
            print(f"Inside Temperature= {temperature_inside:.1f}°C")
            sleep(1)

            if float(temperature_inside) > float(temperature_outside):
                if temp:
                    os.system("python3 door_open.py")
                    temp = False
            else:
                temp = True
                  
               

        except (RuntimeError, TypeError, NameError):
            pass
            

def mp3_thread():
    thread=threading.Thread(target=mp3)
    thread.daemon=True
    thread.start()

def getValue_thread():
    thread=threading.Thread(target=getValue)
    thread.daemon=True
    thread.start()    

if __name__ == "__main__":
    mp3_thread()
    getValue_thread()
    temper()
