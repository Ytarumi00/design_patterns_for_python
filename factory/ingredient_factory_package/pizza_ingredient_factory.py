from abc import ABCMeta, abstractmethod
from factory.ingredient_package.dough import Dough
from factory.ingredient_package.sauce import Sauce
from factory.ingredient_package.cheese import Cheese
from factory.ingredient_package.pepperoni import Pepperoni
from factory.ingredient_package.clam import Clam


class PizzaIngredientFactory(metaclass=ABCMeta):
  '''
  This is ABC for PizzaIngredient
  '''
  
  @abstractmethod
  def createDough(self) -> Dough:
    pass
  
  @abstractmethod
  def createSauce(self) -> Sauce:
    pass
  
  @abstractmethod
  def createCheese(self) -> Cheese:
    pass
  
  @abstractmethod
  def createVeggies(self) -> []:
    pass

  @abstractmethod
  def createPepperoni(self) -> Pepperoni:
    pass
  
  @abstractmethod
  def createClam(self) -> Clam:
    pass
  
  
  