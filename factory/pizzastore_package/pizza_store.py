

from abc import ABCMeta,abstractmethod
from factory import pizzastore_package
from factory.pizza_package.pizza import Pizza

class PizzaStore(metaclass=ABCMeta):
  '''
  This class is ABC for pizza Store
  '''
  def orderPizza(self, type: str) -> Pizza: 
    pizza = self.createPizza(type)
    
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    
    return pizza
    
  @abstractmethod
  def createPizza(self, type: str) -> Pizza:
    pass
  
  
    
  