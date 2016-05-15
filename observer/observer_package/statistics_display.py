from observer.observer_package.observer import Observer
from observer.observer_package.display_element import DisplayElement
from datetime import date


class StatisticsDisplay(Observer, DisplayElement):
  '''
  This class display statistics Conditions
  '''
  
  def __init__(self, weatherData):
    '''
    Init method
    
    Args:
      weatherData: register self instance

    '''
    self.temperature = []
    self.last_update = date.today()
    self.weatherData = weatherData
    self.weatherData.registerObserver(self)

  def update(self, temp, humidity, pressure):
    '''
    IF last_update is equal today,
    updating temperature.
    And then display staticstics temperature.
    Args:
      temp: temperature
      humidity:
      pressure:
   ''' 
    if(self.last_update == date.today()):
      self.temperature.append(temp)
      self.display()
    else:
      self.last_update = date.today()
      self.temperature.clear()
      
      self.temperature.append(temp)
      self.display()
      
  def display(self):
    '''
    displaing statistics temperature.
    '''
    ave = lambda lists: sum(lists) / len(lists)
    print("平均/最高/最低気温: {0: .1f}/{1: .1f}/{2: .1f}".format(ave(self.temperature),
                                max(self.temperature), min(self.temperature)))
    
