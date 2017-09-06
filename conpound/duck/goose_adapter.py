from goose import Goose
from observable import Observable
from observer import Observer
from quackable import Quackable


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose):
        self.goose = goose
        self.observable = Observable(self)

    def quack(self):
        self.goose.honk()
        self.notify_observers()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def __str__(self):
        return "Goose pretending to be a Duck"
