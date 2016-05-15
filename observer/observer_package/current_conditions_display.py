from observer.observer_package.observer import Observer
from observer.observer_package.display_element import DisplayElement


class CurrentConditionDisplay(Observer, DisplayElement):
  '''
  This class display Current Conditions
  '''
  
  def __init__(self, weatherData):
    '''
    Init method
    
    Args:
      weatherData: register self instance

    '''
    self.temperature = None
    self.humidity = None
    self.weatherData = weatherData
    self.weatherData.registerObserver(self)

  def update(self, temp, humidity, pressure):
    '''
    updating temperature and numidity, and then display.
    
    Args:
      temp: temperature
      humidity:
      pressure:
   ''' 
    
    self.temperature = temp
    self.humidity = humidity
    self.display()
    
  def display(self):
    '''
    displaing current temperature and humidity.
    '''
    print("現在の気象状況: 温度　{self.temperature}度　湿度 　{self.humidity}%".format(**locals()))
    
