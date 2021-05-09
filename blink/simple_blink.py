import RPi.GPIO as GPIO
from time import sleep

GPIO_PIN = 14

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (GPIO_PIN, GPIO.OUT, initial=GPIO.LOW)

while(1):
        print ("Blink")
	GPIO.output (GPIO_PIN, GPIO.HIGH)
	sleep (2)
	GPIO.output (GPIO_PIN, GPIO.LOW)
	sleep (2)
