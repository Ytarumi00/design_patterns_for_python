from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
  '''
  This class is subject Pattern
  '''

  @abstractmethod
  def registerObserver(self, ob):
    '''
    This method register Observer instance
    
    Args:
      ob: Observer instance is registed
      
    Returns:
      None
    '''

    pass
    
  @abstractmethod
  def removeObserver(self, ob):
    '''
    This method remove OBserver instance
   
    Args:
      ob: Observer instance is removed
     
    Returns:
      None
    '''

    pass

  @abstractmethod
  def notifyObserver(self):
    '''
    This method notify observer of status when status modify
    '''

    pass
    