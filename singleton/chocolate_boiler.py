from _winapi import NULL
import threading
import time


class ChocolateBoiler:
  '''
  singleton pattern test
  
  Attributes:
    empty: A boolean indicating if boiler is empty.
    boiled: A boolean indicating if boiler is boiled.
  '''
  
  __unique_instance = NULL
  
  def __new__(cls,t):
    if cls.__unique_instance is NULL:
      time.sleep(t)
      cls.__unique_instance = object.__new__(cls)
    print(cls.__unique_instance)
    return cls.__unique_instance
   
  def __init__(self,t):
    super(ChocolateBoiler, self).__init__()
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
      
class testThread(threading.Thread):
  
  def __init__(self,t):
    super(testThread, self).__init__()
    self.wait_t = t
  def run(self):
    boiler = ChocolateBoiler(self.wait_t)
    boiler.fill()
    boiler.boil()
    

if __name__ == "__main__":
  thread1 = testThread(0)
  thread2 = testThread(2)
  thread1.start()
  thread2.start()