import RPi.GPIO as GPIO

# Define a callback function that will be called by the GPIO
# event system:
def onButton(channel):
    if channel == 23:
        print("Button",channel,"was pressed!")

# Setup GPIO23 as input with internal pull-up resistor to hold it HIGH
# until it is pulled down to GND by the connected button:
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Register an edge detection event on FALLING edge. When this event
# fires, the callback onButton() will be executed. Because of
# bouncetime=500 all edges 500 ms after a first falling edge will be ignored:
GPIO.add_event_detect(23, GPIO.FALLING, callback=onButton, bouncetime=500)

# The script would exit now but we want to wait for the event to occure
# so we block execution by waiting for keyboard input so every key will exit
# this script
input()
