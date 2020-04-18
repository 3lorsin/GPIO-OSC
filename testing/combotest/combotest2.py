import RPi.GPIO as GPIO
import argparse
import random
import time
from pythonosc import udp_client

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_message(message, value):
    client.send_message(message, value)
    time.sleep(.3)

def onButton(channel):
    print("Button",channel,"was pressed!")
    if channel == 23:
        send_message("/ch/01/mix/st", 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.1.105",
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
    help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

GPIO.add_event_detect(23, GPIO.FALLING, callback=onButton, bouncetime=500)

input("Push Enter to Exit at any time.\n")
