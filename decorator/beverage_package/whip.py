
from decorator.beverage_package.condiment_decorator import CondimentDecorator
from decorator.beverage_package.beverage import Beverage
from decorator.beverage_package.beverage import Size


class Whip(CondimentDecorator):
  '''
  This class is concrete class for mocha.
  '''
  
  def __init__(self, beverage):
    CondimentDecorator.__init__(self, beverage)
    
  def getDescription(self):
    return self.beverage.getDescription() + ", whip"
    
  def cost(self):
    if(self.beverage.getSize() == Size.TALL):
      self.unit_price = 0.9
    elif(self.beverage.getSize() == Size.GRANDE):
      self.unit_price = 1.0
    elif(self.beverage.getSize() == Size.VENTI):
      self.unit_price = 1.1
    return self.beverage.cost() + self.unit_price
  