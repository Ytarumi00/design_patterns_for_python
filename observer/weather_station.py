
from observer.weather_package.weather_data import WeatherData
from observer.observer_package.current_conditions_display import CurrentConditionDisplay
from observer.observer_package.statistics_display import StatisticsDisplay

if __name__ == "__main__":
  weatherData = WeatherData()
  
  current_conditions_display = CurrentConditionDisplay(weatherData)
  statistics_display = StatisticsDisplay(weatherData)
  
  
  weatherData.setMeasurements(27, 65, 30.4)
  weatherData.setMeasurements(18, 35, 29.4)
  weatherData.setMeasurements(26, 90, 28.4)
  
  