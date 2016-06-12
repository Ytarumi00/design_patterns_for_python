from factory.pizzastore_package.pizza_store import PizzaStore
from _winapi import NULL
from factory.pizza_package.pizza import Pizza
from factory.ingredient_factory_package.ny_pizza_ingredient_factory import NYPizzaIngredientFactory
from factory.pizza_package.cheese_pizza import CheesePizza
from factory.pizza_package.clam_pizza import ClamPizza

class NYPizzaStore(PizzaStore):

  
  def createPizza(self, type: str)->Pizza:
    self.pizza = None
    self.ingredientFactory = NYPizzaIngredientFactory()
    
    if(type == "cheese"):
      self.pizza = CheesePizza(self.ingredientFactory)
      self.pizza.setName("ニューヨークスタイルチーズピザ")
    elif(type == "clam"):
      self.pizza = ClamPizza(self.ingredientFactory)
      self.pizza.setName("ニューヨークスタイルクラムピザ")
    #===========================================================================
    # elif(type == "veggie"):
    #   return NYStyleVeggiePizza()
    # elif(type == "Clam"):
    #   return NYStyleClamPizza()
    # elif(type == "Pepperoni"):
    #   return NYStylePepperoniPizza()
    #===========================================================================
     
    return self.pizza
