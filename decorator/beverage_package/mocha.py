from decorator.beverage_package.condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):
  '''
  This class is concrete class for mocha.
  '''
  
  def __init__(self, beverage):
    self.beverage = beverage
    self._unit_price = 0.2
    
  def getDescription(self):
    return self.beverage.getDescription() + ", Mocha"
    
  def cost(self):
    return self.beverage.cost() + self._unit_price