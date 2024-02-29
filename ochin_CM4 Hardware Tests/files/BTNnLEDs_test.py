from RPi import GPIO

#CPU Ref Number
GPIO.setmode(GPIO.BCM)

#set GPIO23 and GPIO24 as output
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#set the GPIO4, pin 54 as input
GPIO.setup(4, GPIO.IN)

#endless loop
while (True):
    if GPIO.input(4) == 0:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
    else:
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)