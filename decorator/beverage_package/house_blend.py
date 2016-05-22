from decorator.beverage_package.beverage import Beverage



class HouseBlend(Beverage):
  
  def __init__(self):
    Beverage.__init__(self)
    self.description = "ハウスブレンドコーヒー"
    self.unit_price = 0.89
    
  def cost(self):
    return self.unit_price