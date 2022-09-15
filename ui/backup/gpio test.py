import RPi.GPIO as GPIO
from time import sleep

gpio = GPIO
gpio.setmode(GPIO.BCM)
dlpin1 = 4
dlpin2 = 17
drpin1 = 6
drpin2 = 13
dlenpin = 5
drenpin = 22

hlpin1 = 19
hlpin2 = 26
henpin = 27
fanen = 22
fanin1 = 9

gpio.setup(dlpin1, gpio.OUT)
gpio.setup(dlpin2, gpio.OUT)
gpio.setup(drpin1, gpio.OUT)
gpio.setup(drpin2, gpio.OUT)
gpio.setup(dlenpin, gpio.OUT)
gpio.setup(drenpin, gpio.OUT)
gpio.setup(hlpin1, gpio.OUT)
gpio.setup(hlpin2, gpio.OUT)
gpio.setup(henpin, gpio.OUT)
gpio.output(dlpin1, 0)
gpio.output(dlpin2, 0)
gpio.output(drpin1, 0)
gpio.output(drpin2, 0)
gpio.output(dlenpin, 0)
gpio.output(drenpin, 0)
gpio.output(hlpin1, 0)
gpio.output(hlpin2, 0)
gpio.output(henpin, 0)

try:
    gpio.output(dlpin1, 1)
    print("dlpin1 on")
    sleep(2)
    gpio.output(dlpin1, 0)
    print("dlpin1 off")
    
    gpio.output(dlpin2, 1)
    print("dlpin2 on")
    sleep(2)
    gpio.output(dlpin2, 0)
    print("dlpin2 off")

    gpio.output(drpin1, 1)
    print("drpin1 on")
    sleep(2)
    gpio.output(drpin1, 0)
    print("drpin1 off")

    gpio.output(drpin2, 1)
    print("drpin2 on")
    sleep(2)
    gpio.output(drpin2, 0)
    print("drpin2 off")

    gpio.output(dlenpin, 1)
    print("dlenpin on")
    sleep(2)
    gpio.output(dlenpin, 0)
    print("dlenpin off")

    gpio.output(drenpin, 1)
    print("drenpin on")
    sleep(2)
    gpio.output(drenpin, 0)
    print("drenpin off")

    gpio.output(hlpin1, 1)
    print("hlpin1 on")
    sleep(2)
    gpio.output(hlpin1, 0)
    print("hlpin1 off")

    gpio.output(hlpin2, 1)
    print("hlpin2 on")
    sleep(2)
    gpio.output(hlpin2, 0)
    print("hlpin2 off")

    gpio.output(henpin, 1)
    print("henpin1 on")
    sleep(2)
    gpio.output(henpin, 0)
    print("henpin1 off")

    
except:
    print("End")


