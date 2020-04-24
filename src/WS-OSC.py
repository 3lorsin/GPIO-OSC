#!/usr/bin/env python

import asyncio
#import datetime
#import random
import websockets
import argparse
import time
import json

from pythonosc import udp_client
#from configparser import ConfigParser, ExtendedInterpolation

from pymemcache.client.base import Client
GPIOState = Client(('localhost', 11211))

##########
# Config #
##########

with open('config.json') as config_file:
    config = json.load(config_file)

##########
# Config #
##########

#Pause so the GPIO-OSC.py has time to build the memcache
time.sleep(30)

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
            device          = config['commands'][x]["device"]
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
	# type: (button press, configure)     #
	# data: (JSON DATA)                   #
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

print("Starting WS...")
start_websocket_server = websockets.serve(hello, "192.168.1.101", 5678)

#############
# WEBSOCKET #
#############

asyncio.get_event_loop().run_until_complete(start_websocket_server)
asyncio.get_event_loop().run_forever()
