import argparse
import random
import time

from pythonosc import udp_client

def send_message():
    client.send_message("/ch/01/mix/st", 1)
    time.sleep(1)

#if __name__ == "__main__":
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.1.105",
help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=5005,
help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)
