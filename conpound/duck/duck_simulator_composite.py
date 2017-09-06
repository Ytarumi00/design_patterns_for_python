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

    flock_of_mallards = Flock()

    mallard_duck01 = duck_factory.create_mallard_duck()
    mallard_duck02 = duck_factory.create_mallard_duck()
    mallard_duck03 = duck_factory.create_mallard_duck()
    mallard_duck04 = duck_factory.create_mallard_duck()

    flock_of_mallards.add(mallard_duck01)
    flock_of_mallards.add(mallard_duck02)
    flock_of_mallards.add(mallard_duck03)
    flock_of_mallards.add(mallard_duck04)

    flock_of_ducks.add(flock_of_mallards)

    print("Duck simulator: all simulation")
    simulate(flock_of_ducks)

    print("Duck simulator: mallard duck simulation")
    simulate(flock_of_mallards)

    print("The number of quacks: {}".format(QuackCounter.get_quacks()))


def simulate(duck):
    duck.quack()


if __name__ == "__main__":
    duck_factory = CountingDuckFactory()
    start_simulate(duck_factory)
