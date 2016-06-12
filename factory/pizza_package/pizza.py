from abc import ABCMeta

class Pizza(metaclass=ABCMeta):
  '''
  This is ABC for Pizza
  '''
  
  def __init__(self):
    self.name = None
    self.dough = None
    self.sauce = None
    self.toppings = []
    
  def prepare(self):
    print(self.name + "を下処理")
    print("生地をこねる...")
    print("ソース追加...")
    print("トッピングを追加...")
    for topping in self.toppings:
      print(" " + topping)
    
  def bake(self):
    print("350度で25分焼く")
    
  def cut(self):
    print("ピザを扇形に切り分ける")
    
  def box(self):
    print("PizzaStoreの正式な箱に入れる")
    
  def getName(self) -> str:
    return self.name