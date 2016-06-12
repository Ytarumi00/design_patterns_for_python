from abc import ABCMeta

class Cheese(metaclass=ABCMeta):
  pass

class ReggianoCheese(Cheese):
  def __init__(self):
    print("レジューノチーズ")

class MozzarellaCheese(Cheese):
  def __init__(self):
    print("モツァレラチーズ")