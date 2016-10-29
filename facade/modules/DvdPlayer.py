'''
Created on 2016/12/27

@author: yu-suke
'''


class DvdPlayer(object):
    '''
    DvdPlayer class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.amplifier = None

    def on(self):
        print("turn on dvd player")

    def off(self):
        print("turn off dvd player")

    def eject(self):
        print("eject dvd")

    def pause(self):
        print("dvd player pause")

    def play(self, name):
        print("dvd player play {}".format(name))

    def set_surround_audio(self):
        pass

    def set_two_channel_audio(self):
        pass

    def stop(self):
        print("dvd player stop")
