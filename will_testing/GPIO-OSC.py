#!/usr/bin/env python

import argparse
import time
import json
import RPi.GPIO as GPIO
import time

from pythonosc import udp_client

##########
# Config #
##########

with open('config.json') as config_file:
    config = json.load(config_file)

##########
# Config #
##########



###############
# Send Output #
###############

def send_OSC(json_raw):
    data = json.loads(json_raw)
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default=data["ip"],
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=data["port"],
        help="The port the OSC server is listening on")
        args = parser.parse_args()

        client = udp_client.SimpleUDPClient(args.ip, args.port)

        client.send_message(data["command"], data["value"])

    print('OSC Command Received: '+ json_raw);

def button_pressed(GPIO, state):
    button_commands = config['GPIO'][i]["commands"]
    # Run each command
    for x in button_commands:
        if (x != ""):
            current_command = config['commands'][x]["command"]
            device = config['commands'][x]["device"]
            current_value   = config['commands'][x][state]
            current_ip      = config['osc_devices'][device]["ip"]
            current_port    = config['osc_devices'][device]["port"]
            # if command state is null, do not run
            if (current_value != "null"):
                send_OSC('{ "command":"'+ current_command + '" , "value":'+ current_value+', "ip":"'+current_ip+'", "port":"'+current_port+'" }')
                print("Command Executed" + x)


###############
# Send Output #
###############

########
# GPIO #
########

GPIO.setmode(GPIO.BOARD)

for i in config['GPIO']:
    x = int(config['GPIO'][i]['GPIO-type'])
    y = int(config['GPIO'][i]['GPIO-Port'])
    GPIO.setup(y,x)


GPIOState = {"test":"win"}
for i in config['GPIO']:
    x = int(config['GPIO'][i]['GPIO-Port'])
    GPIOState[i] = GPIO.input(x)

try:
    while True:
        for i in config['GPIO']:
            x = int(config['GPIO'][i]['GPIO-Port'])
            y = config['GPIO'][i]['commands']
            z = int(config['GPIO'][i]['LED-IND'])
            if (config['GPIO'][i]['GPIO-type'] == "1"):
                if GPIO.input(x) == 1 and GPIOState[i] == 0:
                    button_pressed(i, "off")
                    print(i + ": Off")
                    if (z != 0):
                        GPIO.output(z, True)
                    GPIOState[i] = 1
                    time.sleep(.1)
                if GPIO.input(x) == 0 and GPIOState[i] == 1:
                    button_pressed(i, "on")
                    print(i + ": On")
                    if (z != 0):
                        GPIO.output(z, False)
                    GPIOState[i] = 0
                    time.sleep(.1)
finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()

########
# GPIO #
########
