'''
Created on 2016/12/27

@author: yu-suke
'''
from facade.modules.Amplifier import Amplifier
from facade.modules.DvdPlayer import DvdPlayer
from facade.modules.CdPlayer import CdPlayer
from facade.modules.Projector import Projector
from facade.modules.Screen import Screen
from facade.modules.TheaterLights import TheaterLights
from facade.modules.PopcornPopper import PopcornPopper
from facade.modules.Tuner import Tuner


class HomeTheaterFacade(object):
    '''
    HomeTheaterFacade class
    '''

    def __init__(self, amp: Amplifier, tuner: Tuner, dvd: DvdPlayer,
                 cd: CdPlayer, projector: Projector, screen: Screen,
                 lights: TheaterLights, popper: PopcornPopper):
        '''
        Constructor
        '''

        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie):
        print("Be preparing to watch movie ...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_surround_sound()
        self.amp.set_volume(8)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Be stopping to watch movie")
        self.popper.off()
        self.lights.on()
        self.screen.down()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

if __name__ == "__main__":
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    cd = CdPlayer()
    projector = Projector()
    screen = Screen()
    lights = TheaterLights()
    popper = PopcornPopper()

    home_theater = HomeTheaterFacade(amp=amp, tuner=tuner, dvd=dvd, cd=cd,
                                     projector=projector, screen=screen,
                                     lights=lights, popper=popper)
    home_theater.watch_movie("レイダース/失われたアーク")
    home_theater.end_movie()
