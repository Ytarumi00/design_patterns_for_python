from abc import ABCMeta

class Sauce(metaclass=ABCMeta):
  pass

class MarinaraSauce(Sauce):
  def __init__(self):
    print("マリナーラソーズ")
  
class PlamTomatoSauce(Sauce):
  def __init__(self):
    print("プラムトマトソース")