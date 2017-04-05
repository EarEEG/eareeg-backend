#!venv/bin/python
''' websocket_data_collector.py

This script uses websockets to transmit data collected by the NeuroPy module to a remote server.
'''

import NeuroPy.NeuroPy as NP
import websocket
import json
import click
import time
from threading import Lock

CLIENT_ID = "CLIENT1"

# declare this globally
ws = None
lock = None
x_count = 0
TIME = -1
SERIAL_PORT = None


def on_connect():
    print("connected")

def on_disconnect():
    print("disconnected")

def on_error(ws, error):
    print(error)

def on_callback_response(*args):
    print("On callback response: ", args)

# generic callback function for neuropy
# which sends the data collected over socketio
# no clue if this works yet
def generic_callback(variable_name, variable_val):
    # generate the dictionary to send to the remote server
    # as specified in the doc
    return_dict = {}
    return_dict["message_type"] = "data"
    return_dict["client_id"] = CLIENT_ID

    # for now, do nothing when setting rawData
    if variable_name == "rawData":
        return
    
    return_dict["data"] = [{"type": variable_name, "value": variable_val}]
    #lock.acquire()
    global x_count
    global ws
    ws.send(str(x_count))
    x_count += 1
    #lock.release()

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

def on_open(ws):
    global TIME
    start_data_collection(SERIAL_PORT, TIME)
    ws.close()


@click.command()
@click.argument('websocket_server')
@click.option('--serial_port', default="/dev/tty.MindWaveMobile-SerialPo", help="Serial port of bluetooth headset")
@click.option('--time', default=-1, help="Number of seconds to collect data")
def main(websocket_server, serial_port, time):
    global TIME
    TIME = time

    global SERIAL_PORT
    SERIAL_PORT = serial_port

    global ws

    ws = websocket.WebSocketApp("{}".format(websocket_server), on_message=on_callback_response, on_error=on_error)
    ws.on_open = on_open
    ws.run_forever()
    

    #socketIO.on("connect", on_connect)
    #socketIO.on("disconnected", on_disconnect)
    #start_data_collection(serial_port, time)
    

if __name__ == "__main__":
    main()
