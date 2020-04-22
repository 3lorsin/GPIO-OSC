#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import argparse
import time
import json
import RPi.GPIO as GPIO
import time

from pythonosc import udp_client
from configparser import ConfigParser, ExtendedInterpolation

##########
# Config #
##########

with open('config.json') as config_file:
    config = json.load(config_file)
#print(config['button_1']['commands'])


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

def button_pressed(button_number, button_state):
    button_commands = config['buttons'][button_number]["commands"]
    # Run each command
    for x in button_commands:
        current_command = config['commands'][x]["command"]
        current_value   = config['commands'][x][button_state]
        current_ip      = config['commands'][x]["ip"]
        current_port    = config['commands'][x]["port"]
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
GPIO.setup(16,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(18,GPIO.IN)



B1_state = 0
B2_state = 0
B3_state = 0
async def buttons():
    try:
        while True:
            if GPIO.input(16) == 1 and B1_state == 0:
                print("Button_1 On")
                button_pressed("button_1", "on")
                B1_state = 1
                time.sleep(.1)
            if GPIO.input(16) == 0 and B1_state == 1:
                print("Button_1 Off")
                button_pressed("button_1", "off")
                B1_state = 0
                time.sleep(.1)
            if GPIO.input(15) == 1 and B2_state == 0:
                print("Button_2 On")
                button_pressed("button_2", "on")
                B2_state = 1
                time.sleep(.1)
            if GPIO.input(15) == 0 and B2_state == 1:
                print("Button_2 Off")
                button_pressed("button_2", "off")
                B2_state = 0
                time.sleep(.1)
            if GPIO.input(18) == 1 and B3_state == 0:
                print("Button_3 On")
                button_pressed("button_3", "on")
                B3_state = 1
                time.sleep(.1)
            if GPIO.input(18) == 0 and B3_state == 1:
                print("Button_3 Off")
                button_pressed("button_3", "off")
                B3_state = 0
                time.sleep(.1)
    finally:
        #cleanup the GPIO pins before ending
        GPIO.cleanup()

########
# GPIO #
########




#############
# WEBSOCKET #
#############

async def hello(websocket, path):
    ws_command = await websocket.recv()
    await websocket.send("Config Here")
    print(ws_command)
    print("fired")

	#######################################
	# message handling                    #
	# type: (button press, configure).    #
	# data: (JSON DATA)  #
	#######################################

    ws_json = json.loads(ws_command);

    if (ws_json['type'] == "sendConfig"):
        print('Config')
        response = "config sending"


    if (ws_json['type'] == 'button_press'):
        button_number = ws_json['data'][0]['button']
        button_state = ws_json['data'][0]['state']
        button_pressed(button_number, button_state)
        response = "Command Sent: "+ws_command

	#handle configuration edits here
    if (ws_json['type'] == 'configure'):
        update_config(ws_json['data'][0]['section'], ws_json['data'][0]['option'], ws_json['data'][0]['value'])
        print("Configuration Edited")
        response = "Config Edited"

    await websocket.send(response)
    await asyncio.sleep()

start_websocket_server = websockets.serve(hello, "192.168.2.2", 5678)


#############
# WEBSOCKET #
#############







asyncio.get_event_loop().run_until_complete(start_websocket_server)
asyncio.get_event_loop().run_forever()
asyncio.run_until_complete(buttons)
