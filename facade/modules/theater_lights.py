'''
Created on 2016/12/27

@author: yu-suke
'''


class TheaterLights(object):
    '''
    TheaterLights class
    '''

    def on(self):
        print("turn on theater lights")

    def off(self):
        print("turn off theater lights")

    def dim(self, val):
        print("dim light {}%".format(val))
