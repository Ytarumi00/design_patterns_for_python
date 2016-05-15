from observer.weather_package.subject import Subject


class WeatherData(Subject):
  
  def __init__(self):
    
    self.observers = []
    self.temperature = None
    self.humidity = None
    self.pressure = None
    
  def registerObserver(self, ob):
    
    self.observers.append(ob)
    
  def removeObserver(self, ob):
    
    self.observers.remove(ob)
    
  def notifyObserver(self):
    
    for ob in self.observers:
      ob.update(self.temperature, self.humidity, self.pressure)

  def measurementsChanged(self):
    self.notifyObserver()
    
  def setMeasurements(self, temp, humidity, pressure):
    self.temperature = temp
    self.humidity = humidity
    self.pressure = pressure
    self.measurementsChanged()
    