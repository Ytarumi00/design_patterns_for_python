from factory.pizzastore_package.pizza_store import PizzaStore
from factory.pizzastore_package.ny_pizza_store import NYPizzaStore
from factory.pizzastore_package.chikago_pizza_store import ChikagoPizzaStore
from factory.pizza_package.pizza import Pizza


class PizzaTestDrive:
  '''
  driver for pizza Store
  '''
  ny_store = NYPizzaStore()
  chikago_store = ChikagoPizzaStore()
  
  pizza = ny_store.orderPizza("cheese")
  print("イーサンの注文は {0}\n".format(pizza.getName()))
  
  pizza = ny_store.orderPizza("clam")
  print("イーサンの注文は {0}\n".format(pizza.getName()))

  pizza = chikago_store.orderPizza("cheese")
  print("ジョエルの注文は {0}\n".format(pizza.getName()))
  
  pizza = chikago_store.orderPizza("clam")
  print("ジョエルの注文は {0}\n".format(pizza.getName()))

