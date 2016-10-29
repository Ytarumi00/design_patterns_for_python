'''
Created on 2016/12/27

@author: yu-suke
'''


class Amplifier:
    '''
    Amplifier class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.tuner = None
        self.dvd_player = None
        self.cd_player = None
        self.volume = 5

    def on(self):
        print("turn on amp")

    def off(self):
        print("turn off amp")

    def set_cd(self, cd):
        self.cd_player = cd

    def set_dvd(self, dvd):
        self.dvd_player = dvd

    def set_stereo_sound(self):
        print("set amp to stereo sound")

    def set_surround_sound(self):
        print("set amp to surround sound")

    def set_tuner(self, tuner):
        self.tuner = tuner

    def set_volume(self, volume):
        self.volume = volume
        print("set amp volume to 5")
