from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    '''
    This class is ABC for command
    '''
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
