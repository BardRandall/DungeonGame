from player import Player
from level import Level
from Managers import *
from EventHandler import EventHandler
from GUI import GUI


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.player = Player(self)
        self.bm = BlockManager()
        self.im = ItemManager()
        self.mobs = []
        self.eh = EventHandler(self)
        self.level = Level('level1.json', self.screen, self)
        self.gui = None

    def update(self):
        self.level.update()
        self.player.update()
        for mob in self.mobs:
            mob.update()
        self.eh.handle(None)

    def step(self, direction):
        self.player.step(direction)

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
        #for mob in self.mobs:
            #mob.render()

    def send_event(self, event):
        self.eh.handle(event)
