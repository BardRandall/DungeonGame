from PIL import Image
import pygame.image as pim
from Constants import *


class BasicBlock:

    def __init__(self):
        self.img = None

    def load_image(self, texture_x, texture_y, cid):
        image = Image.open(ASSETS_DIR + 'blocks/tiles{}.png'.format(cid))
        x, y = texture_x * 16, texture_y * 16
        image = image.crop((x, y, x + 16, y + 16))
        self.img = pim.fromstring(image.tobytes('raw', 'RGBA'), (16, 16), 'RGBA')


class BasicItem:

    def __init__(self):
        self.img = None

    def load_image(self, texture_x, texture_y):
        image = Image.open(ASSETS_DIR + 'items/items.png')
        x, y = texture_x * 16, texture_y * 16
        image = image.crop((x, y, x + 16, y + 16))
        self.img = pim.fromstring(image.tobytes('raw', 'RGBA'), (16, 16), 'RGBA')


class BasicMob:

    def __init__(self):
        pass