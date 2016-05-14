from strategy.fly_package.fly_behavior import FlyBehavior
from strategy.quack_package.quack_behavior import QuackBehavior

class Duck():
  def __init__(self):
    self.fly_behavior = FlyBehavior
    self.quack_behavior = QuackBehavior
  
  def set_fly_behavior(self, fb):
    self.fly_behavior = fb

  def set_quack_behavior(self, qb):
    self.quack_behavior = qb

  def perform_fly(self):
    self.fly_behavior.fly(self)
    
  def perform_quack(self):
    self.quack_behavior.quack(self)
    
  