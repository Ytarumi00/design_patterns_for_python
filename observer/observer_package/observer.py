
from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
  '''
  This class is observer Pattern
  '''
  
  @abstractmethod
  def update(self, temp, humidity, pressure):
    '''
    This method is updating display element.
    
    Args:
      temp: Temperature
      humidity: 
      pressure:
      
    '''
    pass
