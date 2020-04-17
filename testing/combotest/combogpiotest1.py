import RPi.GPIO as GPIO
import comboosctest1

def onButton(channel):
    if channel == 23:
        print("Button",channel,"was pressed!")
        comboosctest1.send_message()

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(23, GPIO.FALLING, callback=onButton, bouncetime=500)

input()
