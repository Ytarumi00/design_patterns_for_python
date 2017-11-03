from observer import Observer
from quack_observable import QuackObservable


class Quackologist(Observer):
    def update(self, duck: QuackObservable):
        print("Quackologist: {} just quacked.".format(str(duck)))
