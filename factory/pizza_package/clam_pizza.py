
from abc import abstractmethod
from factory.pizza_package.pizza import Pizza
from factory.ingredient_factory_package.pizza_ingredient_factory import PizzaIngredientFactory

class ClamPizza(Pizza):
  
  def __init__(self, ingredientFactory: PizzaIngredientFactory):
    Pizza.__init__(self)
    self.ingredientFactory = ingredientFactory
    
  def prepare(self):
    print("{0}を下処理".format(self.name))
    self.dough = self.ingredientFactory.createDough()
    self.sauce = self.ingredientFactory.createSauce()
    self.cheese = self.ingredientFactory.createCheese()
    self.Clam = self.ingredientFactory.createClam()
    