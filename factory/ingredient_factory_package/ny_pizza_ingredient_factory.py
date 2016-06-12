from abc import abstractmethod
from factory.ingredient_factory_package.pizza_ingredient_factory import PizzaIngredientFactory
from factory.ingredient_package.cheese import *
from factory.ingredient_package.clam import *
from factory.ingredient_package.dough import *
from factory.ingredient_package.pepperoni import *
from factory.ingredient_package.sauce import *
from factory.ingredient_package.veggie import *


class NYPizzaIngredientFactory(PizzaIngredientFactory):
  
  def createDough(self)-> Dough:
    return ThinCrustDough()
  
  def createSauce(self)->Sauce:
    return MarinaraSauce()
  
  def createCheese(self)->Cheese:
    return ReggianoCheese()
  
  def createVeggies(self)->[]:
    veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
    return veggies
  
  def createPepperoni(self)->Pepperoni:
    return SlicedPepperoni()
  
  def createClam(self)->Clam:
    return FreshClams()
  
  