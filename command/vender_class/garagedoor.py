
class GarageDoor:
  '''
  Vender class for GarageDoor
  '''
  
  def __init__(self, *args):
    self.name = ""
    if len(args) != 0 :
        self.name = args[0]
  
  def up(self):
    print(self.name)
    print("open garage")
    
  def down(self):
    print(self.name)
    print("close garage")
    
  def stop(self):
    print(self.name)
    print("stop garage door")
    
  def lightOn(self):
    print(self.name)
    print("turn the light on")
    
  def lightOff(self):
    print(self.name)
    print("turn the light off")
    
    