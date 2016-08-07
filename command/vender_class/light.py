

class Light:
  '''
  Vender class for Light
  '''
  
  def __init__(self, name):
    self.name = name
  
  def on(self):
    print(self.name)
    print("turn the light on")
    
  def off(self):
    print(self.name)
    print("turn the light off")
    
