from abc import ABCMeta

class Pepperoni(metaclass=ABCMeta):
  pass

class SlicedPepperoni(Pepperoni):
  def __init__(self):
    print("最高級の薄切りペパロニ")
    
    