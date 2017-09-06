from observer import Observer
from quack_observable import QuackObservable
from quackable import Quackable


class Observable(QuackObservable):
    def __init__(self, duck):
        self.observers = []
        self.duck = duck

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.duck)
