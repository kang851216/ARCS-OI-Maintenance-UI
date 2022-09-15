import RPi.GPIO as GPIO
import time

pin1 = 2
flag = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def test(channel):
    global flag
    if flag == False:
        print("interrupt")
        flag = True
    else:
        flage = False

#GPIO.add_event_detect(pin1, GPIO.RISING, callback=test)

try:
    while True:
        if GPIO.input(pin1):
            print("On")
            time.sleep(1)

except KeyboardInterrupt:
    print()
    GPIO.cleanup()