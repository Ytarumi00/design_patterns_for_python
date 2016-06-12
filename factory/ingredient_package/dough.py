from abc import ABCMeta

class Dough(metaclass=ABCMeta):
  pass

class ThinCrustDough(Dough):
  def __init__(self):
    print("薄いクラフト生地")
    
class ThickCrustDough(Dough):
  def __init__(self):
    print("厚いクルフト生地")