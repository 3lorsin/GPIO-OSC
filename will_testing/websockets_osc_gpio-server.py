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

		client.send_message(data["command"], 1)

	print('OSC Command Received: '+ json_raw);




#WEBSOCKET HANDLER#

async def hello(websocket, path):
    name = await websocket.recv()
    send_OSC(name)

    response = f"Command Sent: {name}!"

    await websocket.send(response)

start_websocket_server = websockets.serve(hello, "127.0.0.1", 5678)

#WEBSOCKET HANDLER#






asyncio.get_event_loop().run_until_complete(start_websocket_server)
asyncio.get_event_loop().run_forever()