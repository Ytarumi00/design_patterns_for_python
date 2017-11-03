from abc import ABCMeta, abstractmethod
from quack_observable import QuackObservable


class Quackable(QuackObservable, metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass
