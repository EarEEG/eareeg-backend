'''
websocket_data_collector.py

This script uses websockets to transmit data collected by the NeuroPy module to a remote server.
'''

import Neuropy.NeuroPy as NP
import socketIO_client
import json

CLIENT_ID = "CLIENT1"
HOST = ""
PORT = 0

BLUETOOTH_SERIAL_PORT_NAME = "/dev/tty.MindWaveMobile-SerialPo"

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
    return_dict = {}
    return_dict["client_id"] = CLIENT_ID

    # for now, do nothing when setting rawData
    if variable_name == "rawData":
        return
    
    return_dict["data"] = [{"type": variable_name, "value": variable_val}]
    socketIO.emit("data", return_dict, on_callback_response)

def start_data_collection(mindwave_serial_port, num_seconds=-1):
    headset_obj = NP.NeuroPy(mindwave_serial_port, 9600, log=False)

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

socketIO = socketIO_client.SocketIO(HOST, PORT, socketIO_client.Logging_Namespace)
socketIO.on("connect", on_connect)
socketIO.on("disconnect", on_disconnect)
start_data_collection(BLUETOOTH_SERIAL_PORT_NAME)
