from Constants import *
from PIL import Image
import pygame.image as pim


class Player:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.absolute_x, self.absolute_y = 0, 0
        self.cell_x = 0
        self.cell_y = 0
        self.img = self._load_image(0, 0)

    @staticmethod
    def _load_image(texture_x, texture_y):
        image = Image.open(ASSETS_DIR + 'player.png')
        x, y = texture_x * 13, texture_y * 16
        image = image.crop((x, y, x + 12, y + 16))
        return pim.fromstring(image.tobytes('raw', 'RGBA'), (12, 16), 'RGBA')

    def _count_absolute_by_cell(self, cell_x, cell_y):
        return cell_x * CELL_SIZE + self.game.level.start_x + 2, \
               cell_y * CELL_SIZE + self.game.level.start_y

    def teleport_to_cell(self, x, y, start_x=None, start_y=None):
        self.cell_x = x
        self.cell_y = y
        if start_x is None or start_y is None:
            self.absolute_x, self.absolute_y = \
                self._count_absolute_by_cell(x, y)
        else:
            self.absolute_x, self.absolute_y = \
                x * CELL_SIZE + start_x + 2, \
                y * CELL_SIZE + start_y

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.img,
                         (self.absolute_x,
                          self.absolute_y))
