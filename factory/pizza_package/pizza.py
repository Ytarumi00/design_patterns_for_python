from abc import ABCMeta, abstractmethod

class Pizza(metaclass=ABCMeta):
  '''
  This is ABC for Pizza
  '''
  
  def __init__(self):
    self.name = None
    self.dough = None
    self.sauce = None
    self.veggies = []
    self.cheese = None
    self.pepperoni = None
    self.Clam = None
    
  @abstractmethod
  def prepare(self):
    pass
    
  def bake(self):
    print("350度で25分焼く")
    
  def cut(self):
    print("ピザを扇形に切り分ける")
    
  def box(self):
    print("PizzaStoreの正式な箱に入れる")
    
  def setName(self, name: str):
    self.name = name
  
  def getName(self) -> str:
    return self.name