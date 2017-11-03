'''
Created on 2017/09/05

@author: yu-suke
'''
from counting_duck_factory import CountingDuckFactory
from duck_call import DuckCall
from flock import Flock
from goose import Goose
from goose_adapter import GooseAdapter
from mallard_duck import MallardDuck
from quack_counter import QuackCounter
from quackable import Quackable
from quackologist import Quackologist
from redhead_duck import RedHeadDuck
from rubber_duck import RubberDuck


def start_simulate(duck_factory):
    redhead_duck = duck_factory.create_redhead_duck()
    duck_call = duck_factory.create_duck_call()
    rubber_duck = duck_factory.create_rubber_duck()
    goose_duck = GooseAdapter(Goose())

    flock_of_ducks = Flock()

    flock_of_ducks.add(redhead_duck)
    flock_of_ducks.add(duck_call)
    flock_of_ducks.add(rubber_duck)
    flock_of_ducks.add(goose_duck)

    quackologist = Quackologist()
    flock_of_ducks.register_observer(quackologist)

    print("Duck simulator: all simulation")
    simulate(flock_of_ducks)

    print("The number of quacks: {}".format(QuackCounter.get_quacks()))


def simulate(duck):
    duck.quack()


if __name__ == "__main__":
    duck_factory = CountingDuckFactory()
    start_simulate(duck_factory)
