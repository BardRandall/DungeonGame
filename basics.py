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

    def get_img(self):
        return self.img

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

    def get_choices(self, game):
        return ['Выбросить'], self.handle_variants

    def get_description(self):
        return 'Автор не придумал описания'


class BasicMob:

    def __init__(self):
        pass


class BasicEffect:

    def __init__(self):
        self.name = 'Неизвестный эффект'

    def affect(self, game):
        pass


class FoodItem(BasicItem):

    def __init__(self):
        super().__init__()

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            game.player.delete_effect('hungry')
            game.player.unhungry_steps = UNHUNGRY_STEPS
            game.player.inventory.remove_item()

    def get_choices(self, game):
        return ['Выбросить', 'Съесть'], self.handle_variants

    def get_description(self):
        return 'Это какая-то еда'


class WeaponItem(BasicItem):

    def __init__(self):
        super().__init__()
        self.name = 'basic_weapon'

    def get_description(self):
        return 'Это какое-то оружие'

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            if game.player.weapon is not None:
                game.player.add_to_inventory(game.player.weapon)
            game.player.weapon = game.player.inventory.get_item()
            game.player.inventory.remove_item()

    def handle_take_off(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            game.player.add_to_inventory(game.player.weapon)
            game.player.weapon = None

    def get_choices(self, game):
        if game.player.weapon.__class__.__name__ == self.name:
            return ['Выбросить', 'Снять'], self.handle_take_off
        return ['Выбросить', 'Надеть'], self.handle_variants


class ArmourItem(BasicItem):

    def __init__(self):
        super().__init__()
        self.name = 'basic_armour'

    def get_description(self):
        return 'Это какая-то броня'

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            if game.player.armour is not None:
                game.player.add_to_inventory(game.player.armour)
            game.player.armour = game.player.inventory.get_item()
            game.player.inventory.remove_item()

    def handle_take_off(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            game.player.add_to_inventory(game.player.armour)
            game.player.armour = None

    def get_choices(self, game):
        if game.player.armour.__class__.__name__ == self.name:
            return ['Выбросить', 'Снять'], self.handle_take_off
        return ['Выбросить', 'Надеть'], self.handle_variants

    def get_defence(self):  # поглощение
        return 0.5


class RingItem(BasicItem):

    def __init__(self):
        super().__init__()
        self.name = 'basic_ring'

    def get_description(self):
        return 'Это какое-то кольцо'

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            if game.player.ring1 is not None:
                game.player.add_to_inventory(game.player.ring1)
            game.player.ring1 = game.player.inventory.get_item()
            game.player.inventory.remove_item()

    def handle_take_off(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            game.player.add_to_inventory(game.player.ring1)
            game.player.ring1 = None

    def get_choices(self, game):
        if game.player.ring1.__class__.__name__ == self.name:
            return ['Выбросить', 'Снять'], self.handle_take_off
        return ['Выбросить', 'Надеть'], self.handle_variants
