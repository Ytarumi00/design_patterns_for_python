
from factory.pizzastore_package.pizza_store import PizzaStore
from _winapi import NULL
from factory.pizza_package.pizza import Pizza
from factory.ingredient_factory_package.chikago_pizza_ingredient_factory import ChikagoPizzaIngredientFactory
from factory.pizza_package.cheese_pizza import CheesePizza
from factory.pizza_package.clam_pizza import ClamPizza

class ChikagoPizzaStore(PizzaStore):
  
  def createPizza(self, type: str)->Pizza:
    self.pizza = None
    self.ingredientFactory = ChikagoPizzaIngredientFactory()
    
    if(type == "cheese"):
      self.pizza = CheesePizza(self.ingredientFactory)
      self.pizza.setName("シカゴスタイルチーズピザ")
    elif(type == "clam"):
      self.pizza = ClamPizza(self.ingredientFactory)
      self.pizza.setName("シカゴスタイルクラムピザ")
    #===========================================================================
    # elif(type == "Veggie"):
    #   return NYStyleVeggiePizza()
    # elif(type == "Clam"):
    #   return NYStyleClamPizza()
    # elif(type == "Pepperoni"):
    #   return NYStylePepperoniPizza()
    #===========================================================================
    
    return self.pizza