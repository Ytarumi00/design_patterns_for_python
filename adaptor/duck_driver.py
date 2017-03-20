'''
Created on 2016/08/13

@author: Y.Tarumi
'''
from adaptor.duck_package.duck import Duck
from adaptor.duck_package.mallard_duck import MallardDuck
from adaptor.adaptor_package.turkey_adaptor import TurkeyAdaptor
from adaptor.turkey_package.wild_turkey import WildTurkey

__author__ = "Y.Tarumi<y.tarumi00+dev@gmail.com>"
__version__ = "1.0.0"
__date__ = "10/28/2016"


def exe_duck(duck: Duck):
    duck.perform_quack()
    duck.perform_fly()


if __name__ == '__main__':
    duck = MallardDuck()

    turkey = WildTurkey()
    turkeyAdaptor = TurkeyAdaptor(turkey)

    print("Turkeyの出力・・・")
    turkey.gobble()
    turkey.fly()

    print("\nDuckの出力・・・")
    exe_duck(duck)

    print("\nTurkeyAdapterの出力・・・")
    exe_duck(turkeyAdaptor)
