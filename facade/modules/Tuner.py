'''
Created on 2016/12/27

@author: yu-suke
'''


class Tuner:
    '''
    Tuner class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.amplifier = None

    def on(self):
        print("turn on tuner")

    def off(self):
        print("turn off tuner")

    def set_am(self, am):
        self.amplifier = am

    def set_fm(self, fm):
        pass

    def set_frequency(self, freq):
        pass
