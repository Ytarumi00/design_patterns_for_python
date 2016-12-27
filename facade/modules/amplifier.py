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
        self.__tuner = None
        self.__dvd_player = None
        self.__cd_player = None
        self.__volume = 5

    def on(self):
        print("turn on amp")

    def off(self):
        print("turn off amp")

    def set_cd(self, cd):
        self.__cd_player = cd

    def set_dvd(self, dvd):
        self.__dvd_player = dvd

    def set_stereo_sound(self):
        print("set amp to stereo sound")

    def set_surround_sound(self):
        print("set amp to surround sound")

    def set_tuner(self, tuner):
        self.__tuner = tuner

    def set_volume(self, volume):
        self.__volume = volume
        print("set amp __volume to 5")
