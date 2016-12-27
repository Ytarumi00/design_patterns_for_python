'''
Created on 2016/12/27

@author: yu-suke
'''
from facade.modules.amplifier import Amplifier
from facade.modules.dvd_player import DvdPlayer
from facade.modules.cd_player import CdPlayer
from facade.modules.projector import Projector
from facade.modules.screen import Screen
from facade.modules.theater_lights import TheaterLights
from facade.modules.popcorn_popper import PopcornPopper
from facade.modules.tuner import Tuner


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

        self.__amp = amp
        self.__tuner = tuner
        self.__dvd = dvd
        self.__cd = cd
        self.__projector = projector
        self.__screen = screen
        self.__lights = lights
        self.__popper = popper

    def watch_movie(self, movie):
        print("Be preparing to watch movie ...")
        self.__popper.on()
        self.__popper.pop()
        self.__lights.dim(10)
        self.__screen.down()
        self.__projector.on()
        self.__projector.wide_screen_mode()
        self.__amp.on()
        self.__amp.set_surround_sound()
        self.__amp.set_volume(8)
        self.__dvd.on()
        self.__dvd.play(movie)

    def end_movie(self):
        print("Be stopping to watch movie")
        self.__popper.off()
        self.__lights.on()
        self.__screen.down()
        self.__projector.off()
        self.__amp.off()
        self.__dvd.stop()
        self.__dvd.eject()
        self.__dvd.off()

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
