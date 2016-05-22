from decorator.beverage_package.beverage import Beverage
from abc import abstractmethod



class CondimentDecorator(Beverage):
  @abstractmethod
  def __init__(self, beverage):
    Beverage.__init__(self)
    self.beverage = beverage
  def getDescription(self):
    pass
  
  def getSize(self):
    return self.beverage.getSize()