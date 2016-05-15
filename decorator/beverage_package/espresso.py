from decorator.beverage_package.beverage import Beverage



class Espresso(Beverage):
  
  
  def __init__(self):
    self.description = "エスプレッソ"
    self.unit_price = 1.99
    
  def cost(self):
    return self.unit_price
  