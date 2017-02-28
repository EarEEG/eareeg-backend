import NeuroPy.NeuroPy as NP
import mindwave_data
import time

# global variable because data collection is done through
# callback functions
global_mindwave_data = mindwave_data.mindwave_data()

# annoyingly long list of callback functions for each 
# individual variable
def attention_callback(attention_value):
    global_mindwave_data.attention_list.append(attention_value)
    return None

def meditation_callback(meditation_value):
    global_mindwave_data.meditation_list.append(meditation_value)
    return None

def rawValue_callback(rawValue_value):
    global_mindwave_data.rawValue_list.append(rawValue_value)
    return None

def delta_callback(delta_value):
    global_mindwave_data.delta_list.append(delta_value)
    return None

def theta_callback(theta_value):
    global_mindwave_data.theta_list.append(theta_value)
    return None

def lowAlpha_callback(lowAlpha_value):
    global_mindwave_data.lowAlpha_list.append(lowAlpha_value)
    return None

def highAlpha_callback(highAlpha_value):
    global_mindwave_data.highAlpha_list.append(highAlpha_value)
    return None

def lowBeta_callback(lowBeta_value):
    global_mindwave_data.lowBeta_list.append(lowBeta_value)
    return None

def highBeta_callback(highBeta_value):
    global_mindwave_data.highBeta_list.append(highBeta_value)
    return None

def lowGamma_callback(lowGamma_value):
    global_mindwave_data.lowGamma_list.append(lowGamma_value)
    return None

def midGamma_callback(midGamma_value):
    global_mindwave_data.midGamma_list.append(midGamma_value)
    return None

def poorSignal_callback(poorSignal_value):
    global_mindwave_data.poorSignal_list.append(poorSignal_value)
    return None

def blinkStrength_callback(blinkStrength_value):
    global_mindwave_data.blinkStrength_list.append(blinkStrength_value)
    return None

# collect_data_points takes the name of a 
# serial port with a MindWave Mobile
# and a number of seconds to collect data points
#
# It connects to the headset and collects all data 
# for that amount of time.
def collect_data_points(mindwave_serial_port, num_seconds):
    object1 = NP.NeuroPy(mindwave_serial_port, 9600, log=False)

    # Register callback functions
    object1.setCallBack("attention", attention_callback)
    object1.setCallBack("meditation", meditation_callback)
    object1.setCallBack("rawValue", rawValue_callback)
    object1.setCallBack("delta", delta_callback)
    object1.setCallBack("theta", theta_callback)
    object1.setCallBack("lowAlpha", lowAlpha_callback)
    object1.setCallBack("highAlpha", highAlpha_callback)
    object1.setCallBack("lowBeta", lowBeta_callback)
    object1.setCallBack("highBeta", highBeta_callback)
    object1.setCallBack("lowGamma", lowGamma_callback)
    object1.setCallBack("midGamma", midGamma_callback)
    object1.setCallBack("poorSignal", poorSignal_callback)
    object1.setCallBack("blinkStrength", blinkStrength_callback)

    # begin taking data
    object1.start()

    # wait for the specified time
    time.sleep(num_seconds)

    # stop taking data
    # because of the callback functions, the mindwave data object should
    # be populated at this point
    object1.stop()

collect_data_points("/dev/tty.MindWaveMobile-SerialPo", 30)
global_mindwave_data.print_list()
