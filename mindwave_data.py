from __future__ import print_function
# mindwave_data.py
# class dedicated to keeping track of data
class mindwave_data(object):
    def __init__(self):
        self.attention_list = []
        self.meditation_list = []
        self.rawValue_list = []
        self.delta_list = []
        self.theta_list = []
        self.lowAlpha_list = []
        self.highAlpha_list = []
        self.lowBeta_list = []
        self.highBeta_list = []
        self.lowGamma_list = []
        self.midGamma_list = []
        self.poorSignal_list = []
        self.blinkStrength_list = []

    def print_vars(self):
        for i, j in vars(self).iteritems():
            print("{} {}".format(i, " ".join([str(x) for x in j])))
