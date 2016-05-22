
from abc import ABCMeta, abstractmethod
from enum import Enum

class AutoNumber(Enum):
  def __new__(self):
    value = len(self.__members__) + 1
    obj = object.__new__(self)
    obj._value_ = value
    return obj
class Size(AutoNumber):
  TALL = ()
  GRANDE = ()
  VENTI = ()


class Beverage(metaclass=ABCMeta):
  '''
  This class is ABC for beverage.
  '''

  
  def __init__(self):
    self.description = "Unkwon beverage"
    self.size = None
    
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

  def setSize(self, value):
    self.size = value
  
  def getSize(self):
    return self.size