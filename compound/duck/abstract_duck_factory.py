from abc import ABCMeta, abstractmethod


class AbstractDuckFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_mallard_duck(self):
        pass

    @abstractmethod
    def create_redhead_duck(self):
        pass

    @abstractmethod
    def create_duck_call(self):
        pass

    @abstractmethod
    def create_rubber_duck(self):
        pass
