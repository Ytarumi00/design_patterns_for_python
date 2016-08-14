from strategy.duck_package.duck import Duck
from strategy.fly_package.fly_with_wings import FlyWithWings
from strategy.quack_package.quack import Quack

class MaddardDuck(Duck):
  def __init__(self):
    self.fly_behavior = FlyWithWings
    self.quack_behavior = Quack
    

if __name__ == "__main__":
  my_duck = MaddardDuck()
  my_duck.perform_fly()
  my_duck.perform_quack()
  
  