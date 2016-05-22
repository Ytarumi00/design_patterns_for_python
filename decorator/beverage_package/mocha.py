from decorator.beverage_package.condiment_decorator import CondimentDecorator
from decorator.beverage_package.beverage import Beverage, Size


class Mocha(CondimentDecorator):
  '''
  This class is concrete class for mocha.
  '''
  
  def __init__(self, beverage):
    CondimentDecorator.__init__(self, beverage)
    
  def getDescription(self):
    return self.beverage.getDescription() + ", Mocha"
    
  def cost(self):
    if(self.beverage.getSize() == Size.TALL):
      self.unit_price = 0.1
    elif(self.beverage.getSize() == Size.GRANDE):
      self.unit_price = 0.2
    elif(self.beverage.getSize() == Size.VENTI):
      self.unit_price = 0.3
    return self.beverage.cost() + self.unit_price
  