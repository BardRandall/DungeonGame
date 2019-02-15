from player import Player
from level import Level
from Managers import *
from EventHandler import EventHandler
import pygame


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.bm = BlockManager()
        self.im = ItemManager()
        self.em = EffectManager()
        self.mm = MobManager()
        self.player = Player(self)
        self.mobs = []
        self.eh = EventHandler(self)
        self.level = Level('level1.json', self.screen, self)
        self.gui = None
        pygame.mixer.music.load('assets/music/theme.mp3')
        #pygame.mixer.music.play(-1)

    def update(self):
        self.level.update()
        self.player.update()
        for mob in self.mobs:
            mob.update()
        self.eh.handle(None)

    def step(self, direction=None):
        if direction is not None:
            self.player.step(direction)
        for mob in self.mobs:
            mob.step()

    def open_gui(self, gui, callback=None):
        if callback is not None:
            self.gui = gui.set_callback(callback)
        else:
            self.gui = gui

    def render(self):
        self.level.render()
        self.player.render()
        if self.gui is not None:
            self.gui.render()
        for mob in self.mobs:
            mob.render()

    def send_event(self, event):
        self.eh.handle(event)
