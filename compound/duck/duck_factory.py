from abstrack_duck_factory import AbstractDuckFactory


class DuckFacktory(AbstractDuckFactory):
    from mallard_duck import MallardDuck
    from redhead_duck import RedHeadDuck
    from duck_call import DuckCall
    from rubber_duck import RubberDuck

    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedHeadDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()
