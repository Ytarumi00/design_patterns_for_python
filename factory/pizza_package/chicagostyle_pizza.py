
from factory.pizza_package.pizza import Pizza

class ChicagoStyleCheesePizza(Pizza):
  
  def __init__(self):
    Pizza.__init__(self)
    self.name = "シカゴ風のディープディッシュチーズピザ"
    self.dough = "極厚クラスト生地"
    self.sauce = "プラムトマトソーズ"
    
    self.toppings.append("刻んだモツァレラチーズ")
    
  def cut(self):
    print("ピザを資格に切り分ける")