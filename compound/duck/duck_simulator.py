'''
Created on 2017/09/05

@author: yu-suke
'''
from quackable import Quackable
from mallard_duck import MallardDuck
from redhead_duck import RedHeadDuck
from duck_call import DuckCall
from rubber_duck import RubberDuck
from goose import Goose
from goose_adapter import GooseAdapter
from quack_counter import QuackCounter
from counting_duck_factory import CountingDuckFactory


def start_simulate(duck_factory):
    mallard_duck = duck_factory.create_mallard_duck()
    redhead_duck = duck_factory.create_redhead_duck()
    duck_call = duck_factory.create_duck_call()
    rubber_duck = duck_factory.create_rubber_duck()
    goose_duck = GooseAdapter(Goose())

    print("Duck simulator")

    simulate(mallard_duck)
    simulate(redhead_duck)
    simulate(duck_call)
    simulate(rubber_duck)
    simulate(goose_duck)

    print("The number of quacks: {}".format(QuackCounter.get_quacks()))


def simulate(duck):
    duck.quack()


if __name__ == "__main__":
    duck_factory = CountingDuckFactory()
    start_simulate(duck_factory)
