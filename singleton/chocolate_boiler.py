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
  mylock = threading.Lock()
  
  def __new__(cls,t):
    cls.mylock.acquire()
    if cls.__unique_instance is NULL:
      time.sleep(t)
      cls.__unique_instance = object.__new__(cls)
      cls.__unique_instance.empty = True
      cls.__unique_instance.boiled = False
    cls.mylock.release()
    print(cls.__unique_instance)
    return cls.__unique_instance
   
  def __init__(self,t):
    super(ChocolateBoiler, self).__init__()
    
  def fill(self):
    if(self.isEmpty()):
      self.mylock.acquire()
      print("牛乳とチョコの混合液を入れる")
      self.empty = False
      self.boiled = False
      print(self.__dict__)
      self.mylock.release()
    else:
      print("#boilerが空でなければ混合液を入れられません")
      
  def drain(self):
    if(not self.isEmpty() and self.isBoiled()):
      self.mylock.acquire()
      print("沸騰した混合液を空にする")
      self.empty = True
      print(self.__dict__)
      self.mylock.release()
    else:
      print("#沸騰していない，混合液がからです")
      
  def boil(self):
    if(not self.isEmpty() and not self.isBoiled()):
      self.mylock.acquire()
      print("中身を沸騰させる")
      self.boiled = True
      print(self.__dict__)
      self.mylock.release()
    else:
      print("#沸騰しているか，混合液がからです")
      
  def isEmpty(self):
    return self.empty
  
  def isBoiled(self):
    return self.boiled
      
class testThread1(threading.Thread):
  
  def __init__(self,t):
    super(testThread1, self).__init__()
    self.wait_t = t
  def run(self):
    boiler = ChocolateBoiler(self.wait_t)
    boiler.fill()
    boiler.boil()
    
class testThread2(threading.Thread):
  
  def __init__(self,t):
    super(testThread2, self).__init__()
    self.wait_t = t
  def run(self):
    boiler = ChocolateBoiler(self.wait_t)
    boiler.fill()
    boiler.boil()

if __name__ == "__main__":
  thread1 = testThread1(5)
  thread2 = testThread2(2)
  thread1.start()
  thread2.start()