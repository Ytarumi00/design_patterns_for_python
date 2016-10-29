'''
Created on 2016/12/27

@author: yu-suke
'''


class Projector(object):
    '''
    Projector class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.dvdplayer = None

    def on(self):
        print("turn on projector")

    def off(self):
        print("turn off projector")

    def tv_mode(self):
        print("projector is tv mode")

    def wide_screen_mode(self):
        print("projector is wide screen mode")
