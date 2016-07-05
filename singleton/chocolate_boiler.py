from _winapi import NULL

class ChocolateBoiler:
  '''
  singleton pattern test
  
  Attributes:
    empty: A boolean indicating if boiler is empty.
    boiled: A boolean indicating if boiler is boiled.
  '''
  
  __unique_instance = NULL
  
  def __new__(cls):
    if cls.__unique_instance is NULL:
      cls.__unique_instance = object.__new__(cls)
    return cls.__unique_instance
  
  def __init__(self):
    self.empty = True
    self.boiled = False
    
  def fill(self):
    if(self.isEmpty()):
      print("牛乳とチョコの混合液を入れる")
      self.empty = False
      self.boiled = False
    else:
      print("#boilerが空でなければ混合液を入れられません")
      
  def drain(self):
    if(not self.isEmpty() and self.isBoiled()):
      print("沸騰した混合液を空にする")
      self.empty = True
    else:
      print("#沸騰していない，混合液がからです")
      
  def boil(self):
    if(not self.isEmpty() and not self.isBoiled()):
      print("中身を沸騰させる")
      self.boiled = True
    else:
      print("#沸騰しているか，混合液がからです")
      
  def isEmpty(self):
    return self.empty
  
  def isBoiled(self):
    return self.boiled
      
if __name__ == "__main__":
  boiler1 = ChocolateBoiler()
  boiler2 = ChocolateBoiler()
  boiler1.fill()
  boiler2.fill()
  boiler1.boil()
  boiler2.boil()
  boiler1.drain()
  boiler2.drain()