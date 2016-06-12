
from factory.pizzastore_package.pizza_store import PizzaStore
from _winapi import NULL
from factory.pizza_package.pizza import Pizza
from factory.pizza_package.chicagostyle_pizza import ChicagoStyleCheesePizza

class ChikagoPizzaStore(PizzaStore):
  
  def createPizza(self, type: str)->Pizza:
    if(type == "cheese"):
      return ChicagoStyleCheesePizza()
    #===========================================================================
    # elif(type == "Veggie"):
    #   return NYStyleVeggiePizza()
    # elif(type == "Clam"):
    #   return NYStyleClamPizza()
    # elif(type == "Pepperoni"):
    #   return NYStylePepperoniPizza()
    #===========================================================================
    else:
      return NULL