
from strategy.duck_package.duck import Duck
from strategy.quack_package.squeak import Squeak
from strategy.fly_package.fly_no_way import FlyNOWay
from strategy.quack_package.quack import Quack

class RubberDuck(Duck):
  def __init__(self):
    self.fly_behavior = FlyNOWay
    self.quack_behavior = Squeak
    

if __name__ == "__main__":
  my_duck = RubberDuck()
  my_duck.perform_fly()
  my_duck.perform_quack()
  my_duck.set_quack_behavior(Quack)
  my_duck.perform_fly()
  my_duck.perform_quack()

  
  