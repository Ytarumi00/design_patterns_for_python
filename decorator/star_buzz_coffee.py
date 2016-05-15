from decorator.beverage_package.beverage import Beverage
from decorator.beverage_package.espresso import Espresso
from decorator.beverage_package.house_blend import HouseBlend
from decorator.beverage_package.mocha import Mocha


if __name__ == "__main__":
  beverage = Espresso()
  print("{0} ${1}".format(beverage.getDescription(),beverage.cost()))
  
  beverage2 = HouseBlend()
  beverage2 = Mocha(beverage2)
  beverage2 = Mocha(beverage2)
  print("{0} ${1}".format(beverage2.getDescription(), beverage2.cost()))
