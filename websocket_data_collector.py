#!venv/bin/python
'''
websocket_data_collector.py

This script uses websockets to transmit data collected by the NeuroPy module to a remote server.
'''

import NeuroPy.NeuroPy as NP
import socketIO_client
import json
import click
from threading import Lock
import time

CLIENT_ID = "CLIENT1"

# declare this globally
socketIO = None
lock = None
x = 0

def on_connect():
    print("connected")

def on_disconnect():
    print("disconnected")

def on_callback_response(*args):
    print("On callback response: ", args)

# generic callback function for neuropy
# which sends the data collected over socketio
def generic_callback(variable_name, variable_val):
    # generate the dictionary to send to the remote server
    # as specified in the doc
    if variable_name == "rawValue":
        return

    global filename
    global x
    if x % 20 == 0:
        print("wrote 20 measurements")
    x += 1
    filename.write("{} {}\n".format(variable_name, variable_val))

def start_data_collection(serial_port, num_seconds=-1):
    headset_obj = NP.NeuroPy(serial_port, 9600, log=False)

    headset_obj.setCallBack("attention", generic_callback)
    headset_obj.setCallBack("meditation", generic_callback)
    headset_obj.setCallBack("rawValue", generic_callback)
    headset_obj.setCallBack("delta", generic_callback)
    headset_obj.setCallBack("theta", generic_callback)
    headset_obj.setCallBack("lowAlpha", generic_callback)
    headset_obj.setCallBack("highAlpha", generic_callback)
    headset_obj.setCallBack("lowBeta", generic_callback)
    headset_obj.setCallBack("highBeta", generic_callback)
    headset_obj.setCallBack("lowGamma", generic_callback)
    headset_obj.setCallBack("midGamma", generic_callback)
    headset_obj.setCallBack("poorSignal", generic_callback)
    headset_obj.setCallBack("blinkStrength", generic_callback)

    headset_obj.start()
    if num_seconds != -1:
        time.sleep(num_seconds)
        headset_obj.stop()

@click.command()
@click.argument('runfile')
#@click.argument('clientid')
@click.option('--serial_port', default="/dev/tty.MindWaveMobile-SerialPo", help="Serial port of bluetooth headset")
@click.option('--time', default=5, help="Number of seconds to collect data")
def main(runfile, serial_port, time):
    global filename
    filename = open("{}".format(runfile), "w")
    start_data_collection(serial_port, time) 

if __name__ == "__main__":
    main()
