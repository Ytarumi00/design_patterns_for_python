from abc import ABCMeta

class Clam(metaclass=ABCMeta):
  pass

class FreshClams(Clam):
  def __init__(self):
    print("新鮮なクラム")
  
class FlozenClams(Clam):
  def __init__(self):
    print("冷凍クラム")