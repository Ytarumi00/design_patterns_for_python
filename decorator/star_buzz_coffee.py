from decorator.beverage_package.beverage import Beverage
from decorator.beverage_package.espresso import Espresso
from decorator.beverage_package.house_blend import HouseBlend
from decorator.beverage_package.mocha import Mocha
from decorator.beverage_package.whip import Whip
from decorator.beverage_package.beverage import Size


if __name__ == "__main__":
  beverage = Espresso()
  print("({0}){1} ${2: .2f}".format(beverage.getSize(), 
                                    beverage.getDescription(), beverage.cost()))
  
  beverage2 = HouseBlend()
  beverage2.setSize(Size.GRANDE)
  beverage2 = Mocha(beverage2)
  beverage2 = Mocha(beverage2)
  print("({0}){1} ${2: .2f}".format(beverage2.getSize(), 
                                    beverage2.getDescription(), beverage2.cost()))

  beverage3 = HouseBlend()
  beverage3.setSize(Size.VENTI)
  beverage3 = Mocha(beverage3)
  beverage3 = Whip(beverage3)
  print("({0}){1} ${2: .2f}".format(beverage3.getSize(), 
                                    beverage3.getDescription(), beverage3.cost()))