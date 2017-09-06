from abc import ABCMeta, abstractmethod
from observer import Observer


class QuackObservable(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
