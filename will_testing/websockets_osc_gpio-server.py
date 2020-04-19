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
	# data: (JSON DATA (config), string)  #
	#######################################

	ws_json = json.loads(ws_command);


	if (ws_json['type'] == 'button_press'):

		# Temp Config
		# button_1 = '{ "command":"/LS/Go/PB/10" , "value":0, "ip":"192.168.2.69", "port":"5005" }'
		# button_2 = '{ "command":"/ch/02/mix/st" , "value":"1", "ip":"127.0.0.1", "port":"5005" }'
		# button_3 = '{ "command":"/ch/03/mix/st" , "value":"1", "ip":"192.168.2.1", "port":"5005" }'
		# button_4 = '{ "command":"/ch/04/mix/st" , "value":"1", "ip":"127.0.0.1", "port":"5005" }'
        #
		# if ws_json['data'] == "button_1": send_OSC(button_1)
		# if ws_json['data'] == "button_2": send_OSC(button_2)
		# if ws_json['data'] == "button_3": send_OSC(button_3)
		# if ws_json['data'] == "button_4": send_OSC(button_4)
		button_command = config.get(ws_json['data'], "command")
		button_value   = config.get(ws_json['data'], "value")
		button_ip      = config.get(ws_json['data'], "ip")
		button_port    = config.get(ws_json['data'], "port")
		send_OSC('{ "command":"'+ button_command + '" , "value":'+ button_value+', "ip":"'+button_ip+'", "port":"'+button_port+'" }')


	#handle configuration edits here
	if (ws_json['type'] == 'configure'):
                #print("winning")
                update_config(ws_json['data'][0]['section'], ws_json['data'][0]['option'], ws_json['data'][0]['value'])
                #print(ws_json['data'][0]['ip'])

	response = "Command Sent: "+ws_command

	await websocket.send(response)



start_websocket_server = websockets.serve(hello, "192.168.2.2", 5678)


#############
# WEBSOCKET #
#############






asyncio.get_event_loop().run_until_complete(start_websocket_server)
asyncio.get_event_loop().run_forever()
