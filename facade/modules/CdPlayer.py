'''
Created on 2016/12/27

@author: yu-suke
'''


class CdPlayer(object):
    '''
    CdPlayer class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__amplifier = None

    def on(self):
        print("turn on cd player")

    def off(self):
        print("turn off cd player")

    def eject(self):
        print("eject cd")

    def pause(self):
        print("cd player pause")

    def play(self, name):
        print("cd player play {}".format(name))

    def stop(self):
        print("cd player stop")
