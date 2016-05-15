from decorator.beverage_package.beverage import Beverage
from abc import abstractmethod



class CondimentDecorator(Beverage):
  @abstractmethod
  def getDescription(self):
    pass