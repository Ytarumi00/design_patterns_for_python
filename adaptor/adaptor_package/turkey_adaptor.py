'''
Created on 2016/08/13

@author: yu-suke
'''
from adaptor.duck_package.duck import Duck
from adaptor.turkey_package.turkey import Turkey

class TurkeyAdaptor(Duck):
    '''
    Adaptor for conversion of Turkey into Duck
    '''

    def __init__(self, turkey: Turkey):
        '''
        Set turkey instance
        '''
        self.turkey = turkey
        
    def quack(self):
        