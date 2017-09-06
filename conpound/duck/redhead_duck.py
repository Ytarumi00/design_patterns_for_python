from observable import Observable
from observer import Observer
from quackable import Quackable


class RedHeadDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Ga-Ga-")
        self.notify_observers()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def __str__(self):
        return "redhead duck"
