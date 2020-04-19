#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import argparse
import time
import json

from pythonosc import udp_client
from configparser import ConfigParser, ExtendedInterpolation

################
# ConfigParser #
################

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('config.ini')


def update_config(section, option, value):
        config.set(section, option, value)
        with open('./config.ini', 'w') as f:
              config.write(f)
              print(config.get("settings", "ip"))

print(config.sections())

#Update Config and save
update_config("settings", "ip", "8.8.8.8")

################
# ConfigParser #
################



############
# Send OSC #
############

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

############
# Send OSC #
############



#############
# WEBSOCKET #
#############

async def hello(websocket, path):
	ws_command = await websocket.recv()
	print(ws_command)

	#######################################
	# message handling                    #
	# type: (button press, configure).    #
	# data: (JSON DATA)  #
	#######################################

	ws_json = json.loads(ws_command);


	if (ws_json['type'] == 'button_press'):

        # Get button and state
		button_number = ws_json['data'][0]['button']
		button_state = ws_json['data'][0]['state']
		button_commands = json.loads(config.get(button_number, "commands"))
        # Run each command
		for x in button_commands:
			current_command = config.get(x, "command")
			current_value   = config.get(x, button_state)
			current_ip      = config.get(x, "ip")
			current_port    = config.get(x, "port")
            # if command state is null, do not run
			if (current_value != "null"):
			    send_OSC('{ "command":"'+ current_command + '" , "value":'+ current_value+', "ip":"'+current_ip+'", "port":"'+current_port+'" }')
			    print("Command Executed" + x)

	#handle configuration edits here
	if (ws_json['type'] == 'configure'):
                update_config(ws_json['data'][0]['section'], ws_json['data'][0]['option'], ws_json['data'][0]['value'])
                print("Configuration Edited")

	response = "Command Sent: "+ws_command

	await websocket.send(response)



start_websocket_server = websockets.serve(hello, "192.168.2.2", 5678)


#############
# WEBSOCKET #
#############


asyncio.get_event_loop().run_until_complete(start_websocket_server)
asyncio.get_event_loop().run_forever()
