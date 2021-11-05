import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pirPin = 7
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

while True:
    if GPIO.input(pirPin) == GPIO.LOW:
        print "모션이 감지되었습니다!"

    else:
        print "모션이 감지되지 않았습니다."
    time.sleep(0.2)
