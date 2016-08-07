'''
Created on 2016/08/05

@author: yu-suke
'''

class Stereo:
    '''
    Vender class for Stereo
    '''


    def __init__(self, *args):
        self.name = args[0]
    
    def on(self):
        print(self.name)
        print("turn on stereo")
        
    def off(self):
        print(self.name)
        print("turn off stereo")
        
    def setCD(self):
        print(self.name)
        print("set CD")
        
    def setRadio(self):
        print(self.name)
        print("set radio")
        
    def setVolume(self, vol):
        print(self.name)
        print("set volume at {}".format(vol))
        
        
