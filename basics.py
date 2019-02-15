from PIL import Image
import pygame.image as pim
from Constants import *
import pygame


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

    def load_own_image(self, img, texture_x, texture_y):
        image = Image.open(img)
        x, y = texture_x * 16, texture_y * 16
        image = image.crop((x, y, x + 16, y + 16))
        self.img = pim.fromstring(image.tobytes('raw', 'RGBA'), (16, 16), 'RGBA')

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()

    def get_choices(self, game):
        return ['Выбросить'], self.handle_variants

    def get_description(self):
        return 'Автор не придумал описания'


class BasicMob:

    def __init__(self, game):
        self.game = game
        self.img = None
        self.health = 5
        self.raduis = 5
        self.cell_x = 0
        self.cell_y = 0
        self.absolute_x = 0
        self.absolute_y = 0
        self.moving_animation = []

        self.facing = RIGHT
        self.moving = None
        self.moving_state = 0

    @staticmethod
    def load_image(texture_x, texture_y, file):
        image = Image.open(ASSETS_DIR + 'mobs/' + file)
        x, y = texture_x * 16, texture_y * 16
        image = image.crop((x, y, x + 16, y + 16))
        return pim.fromstring(image.tobytes('raw', 'RGBA'), (16, 16), 'RGBA')

    def load_animation(self, animation, y, file):
        for i in animation:
            self.moving_animation.append(self.load_image(i, y, file))

    def _count_absolute_by_cell(self, cell_x, cell_y):
        return cell_x * CELL_SIZE + self.game.level.start_x, \
               cell_y * CELL_SIZE + self.game.level.start_y - 3

    def _update_cell(self, bench=None):
        pass

    def teleport_to_cell(self, x, y, start_x=None, start_y=None):
        self.cell_x = x
        self.cell_y = y
        if start_x is None or start_y is None:
            self.absolute_x, self.absolute_y = \
                self._count_absolute_by_cell(x, y)
            self._update_cell()
        else:
            self.absolute_x, self.absolute_y = \
                x * CELL_SIZE + start_x, \
                y * CELL_SIZE + start_y - 3
            self._update_cell()

    def step(self):
        if self.moving is None:
            return
        self.img = self.moving_animation[self.moving_state]
        if self.facing == LEFT:
            self.img = pygame.transform.flip(self.img, 1, 0)
        if self.moving == UP:
            self.absolute_y -= 2
        elif self.moving == RIGHT:
            self.absolute_x += 2
        elif self.moving == DOWN:
            self.absolute_y += 2
        elif self.moving == LEFT:
            self.absolute_x -= 2
        if self.moving_state < len(self.moving_animation) - 1:
            self.moving_state += 1
        else:
            if self.moving == UP:
                self.cell_y -= 1
            elif self.moving == RIGHT:
                self.cell_x += 1
            elif self.moving == DOWN:
                self.cell_y += 1
            elif self.moving == LEFT:
                self.cell_x -= 1
            self.moving = None
            self.moving_state = 0
            self.teleport_to_cell(self.cell_x, self.cell_y)

    def update(self):
        if self.moving is None:
            return
        self.img = self.moving_animation[self.moving_state]
        if self.facing == LEFT:
            self.img = pygame.transform.flip(self.img, 1, 0)
        if self.moving == UP:
            self.absolute_y -= 2
        elif self.moving == RIGHT:
            self.absolute_x += 2
        elif self.moving == DOWN:
            self.absolute_y += 2
        elif self.moving == LEFT:
            self.absolute_x -= 2
        if self.moving_state < len(self.moving_animation) - 1:
            self.moving_state += 1
        else:
            if self.moving == UP:
                self.cell_y -= 1
            elif self.moving == RIGHT:
                self.cell_x += 1
            elif self.moving == DOWN:
                self.cell_y += 1
            elif self.moving == LEFT:
                self.cell_x -= 1
            self.moving = None
            self.moving_state = 0
            self.teleport_to_cell(self.cell_x, self.cell_y)

    def render(self):
        self.game.screen.blit(self.img, (self.absolute_x, self.absolute_y))


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

    def put_on_event(self, game):
        pass

    def take_off_event(self, game):
        pass

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            if game.player.weapon is not None:
                game.player.add_to_inventory(game.player.weapon)
            game.player.weapon = game.player.inventory.get_item()
            game.player.inventory.remove_item()
            self.put_on_event(game)

    def handle_take_off(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            game.player.add_to_inventory(game.player.weapon)
            game.player.weapon = None
            self.take_off_event(game)

    def get_choices(self, game):
        if game.player.weapon.__class__.__name__ == self.name:
            return ['Выбросить', 'Снять'], self.handle_take_off
        return ['Выбросить', 'Надеть'], self.handle_variants

    def get_damage(self):
        return 3


class ArmourItem(BasicItem):

    def __init__(self):
        super().__init__()
        self.name = 'basic_armour'

    def get_description(self):
        return 'Это какая-то броня'

    def put_on_event(self, game):
        pass

    def take_off_event(self, game):
        pass

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            if game.player.armour is not None:
                game.player.add_to_inventory(game.player.armour)
            game.player.armour = game.player.inventory.get_item()
            game.player.inventory.remove_item()
            self.put_on_event(game)

    def handle_take_off(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            game.player.add_to_inventory(game.player.armour)
            game.player.armour = None
            self.take_off_event(game)

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

    def put_on_event(self, game):
        pass

    def take_off_event(self, game):
        pass

    def handle_variants(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            if game.player.ring1 is not None:
                game.player.add_to_inventory(game.player.ring1)
            game.player.ring1 = game.player.inventory.get_item()
            game.player.inventory.remove_item()
            self.put_on_event(game)

    def handle_take_off(self, variant, game):
        if variant == 0:
            game.player.inventory.throw_item()
        elif variant == 1:
            game.player.add_to_inventory(game.player.ring1)
            game.player.ring1 = None
            self.take_off_event(game)

    def get_choices(self, game):
        if game.player.ring1.__class__.__name__ == self.name:
            return ['Выбросить', 'Снять'], self.handle_take_off
        return ['Выбросить', 'Надеть'], self.handle_variants
