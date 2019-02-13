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

    def can_go(self):
        return True

    def go_into_event(self, game):
        return True

    def go_out_event(self, game):
        return True


class BasicItem:

    def __init__(self):
        self.img = None

    def load_image(self, texture_x, texture_y):
        image = Image.open(ASSETS_DIR + 'items/items.png')
        x, y = texture_x * 16, texture_y * 16
        image = image.crop((x, y, x + 16, y + 16))
        self.img = pim.fromstring(image.tobytes('raw', 'RGBA'), (16, 16), 'RGBA')

    def take_item_event(self, game):
        return True

    def throw_item_event(self, game):
        return True

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()

    def get_choices(self):
        return ['Выбросить'], self.handle_variants

    def get_description(self):
        return 'Автор не придумал описания'


class BasicMob:

    def __init__(self):
        pass
