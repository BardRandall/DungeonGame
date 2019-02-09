from player import Player
from level import Level
from Managers import *


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.player = Player(self)
        self.bm = BlockManager()
        self.im = ItemManager()
        self.mobs = []
        self.level = Level('level1.json', self.screen, self)

    def update(self):
        self.level.update()
        self.player.update()
        for mob in self.mobs:
            mob.update()

    def render(self):
        self.level.render()
        self.player.render()
        #for mob in self.mobs:
            #mob.render()

    def send_event(self, event):
        pass
