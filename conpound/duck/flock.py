from observer import Observer
from quackable import Quackable


class Flock(Quackable):

    def __init__(self):
        self.quackers = []

    def add(self, quacker: Quackable):
        self.quackers.append(quacker)

    def quack(self):
        for quaker in self.quackers:
            quaker.quack()

    def register_observer(self, observer: Observer):
        for quaker in self.quackers:
            quaker.register_observer(observer)

    def notify_observers(self):
        pass
