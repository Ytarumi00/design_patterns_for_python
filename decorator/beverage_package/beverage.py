
from abc import ABCMeta, abstractmethod

class Beverage(metaclass=ABCMeta):
  '''
  This class is ABC for beverage.
  '''
  
  def __init__(self):
    self.description = "Unkwon beverage"
    
  def getDescription(self):
    '''
    This method display description.
    '''
    return self.description
  
  
  @abstractmethod
  def cost(self):
    '''
    This method Calculate cost
    '''
    pass