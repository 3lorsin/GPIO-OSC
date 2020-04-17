# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO

def button_callback(channel):
    print("Button was pushed!")

# Ignore warning for now
#GPIO.setwarnings(False)

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Set pin 16 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Setup event on pin 16 rising edge
GPIO.add_event_detect(16,GPIO.RISING,callback=button_callback)

# Run until someone presses enter
message = input("Press enter to quit\n\n")

# Clean up
GPIO.cleanup()
