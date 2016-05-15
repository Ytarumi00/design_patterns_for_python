from abc import abstractmethod, ABCMeta


class DisplayElement(metaclass=ABCMeta):
  '''
  This is abc for display element.
  '''
  
  @abstractmethod
  def display(self):
    '''
    This method display elements.
    '''
