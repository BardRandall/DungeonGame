from Constants import *
from PIL import Image
import pygame.image as pim
import pygame

from GUI import Inventory


class Player:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.health = MAX_HEALTH
        self.effects = []
        self.unhungry_steps = UNHUNGRY_STEPS

        self.absolute_x, self.absolute_y = 0, 0
        self.cell_x = 0
        self.cell_y = 0
        self.img = self._load_image(0, 0)

        self.wearing = 1

        self.weapon = None
        self.armour = None
        self.ring1 = None
        self.ring2 = None

        self.moving_animation = []
        for i in [0, 2, 3, 4, 5, 6, 7, 0, 0]:
            self.moving_animation.append(self._load_image(i, self.wearing))
        self.facing = RIGHT
        self.moving = None
        self.moving_state = 0
        self.show_inventory = False

        self.inventory = Inventory(self.game)

    @staticmethod
    def _load_image(texture_x, texture_y):
        image = Image.open(ASSETS_DIR + 'player.png')
        x, y = texture_x * 12, texture_y * 15
        image = image.crop((x, y, x + 12, y + 15))
        return pim.fromstring(image.tobytes('raw', 'RGBA'), (12, 15), 'RGBA')

    def _count_absolute_by_cell(self, cell_x, cell_y):
        return cell_x * CELL_SIZE + self.game.level.start_x + 2, \
               cell_y * CELL_SIZE + self.game.level.start_y

    def add_to_inventory(self, item):
        if len(self.inventory.store) < MAX_ITEMS:
            if type(item) != str:
                self.inventory.append(item)
            else:
                self.inventory.append(self.game.im.items_store[item])
            return True
        return False

    def set_effect(self, effect):
        obj = self.game.em.find(effect)
        if obj not in self.effects:
            self.effects.append(obj)

    def delete_effect(self, effect):
        eff = self.game.em.find(effect)
        if eff in self.effects:
            del self.effects[self.effects.index(eff)]

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
                y * CELL_SIZE + start_y - 1

    def hit(self, k):
        if self.armour is None:
            self.health -= k
            return
        self.health -= (1 - self.armour.get_defence()) * k

    def _update_cell(self):
        cell = self.game.level.board[self.cell_x][self.cell_y]
        if not cell.items:
            return
        for item in cell.items:
            if not self.game.im.summon_event(item['item'], TAKE_ITEM_EVENT, self.game):
                continue
            if self.add_to_inventory(self.game.im.items_store[item['item']]):
                del cell.items[cell.items.index(item)]
            else:
                break

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
            self.game.bm.summon_event(self.game.level.board[self.cell_x][self.cell_y].block,
                                      GO_OUT_EVENT, self.game)
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
            self.game.bm.summon_event(self.game.level.board[self.cell_x][self.cell_y].block,
                                      GO_INTO_EVENT, self.game)
            self.teleport_to_cell(self.cell_x, self.cell_y)

    def render(self):
        self.screen.blit(self.img,
                         (self.absolute_x,
                          self.absolute_y))
        if self.show_inventory:
            self.inventory.render()
        if self.unhungry_steps > 0:
            pygame.draw.rect(self.game.screen, (255, 255, 0), (
                0,
                0,
                int((self.unhungry_steps / UNHUNGRY_STEPS) * WIDTH),
                HUNGRYBAR_HEIGHT
            ))
        pygame.draw.rect(self.game.screen, (255, 0, 0), (
            0,
            HUNGRYBAR_HEIGHT,
            int((self.health / MAX_HEALTH) * WIDTH),
            HUNGRYBAR_HEIGHT
        ))

    def step(self, direction):
        if self.moving is not None:
            return
        if direction == LEFT:
            self.facing = LEFT
        elif direction == RIGHT:
            self.facing = RIGHT
        if direction == UP and \
                not self.game.bm.summon_event(
                    self.game.level.board[self.cell_x][self.cell_y - 1].block,
                    CAN_GO_EVENT, self.game):
            return
        elif direction == RIGHT and \
                not self.game.bm.summon_event(
                    self.game.level.board[self.cell_x + 1][self.cell_y].block,
                    CAN_GO_EVENT, self.game):
            return
        elif direction == DOWN and \
                not self.game.bm.summon_event(
                    self.game.level.board[self.cell_x][self.cell_y + 1].block,
                    CAN_GO_EVENT, self.game):
            return
        elif direction == LEFT and \
                not self.game.bm.summon_event(
                    self.game.level.board[self.cell_x - 1][self.cell_y].block,
                    CAN_GO_EVENT, self.game):
            return
        self.moving = direction
        self.unhungry_steps -= 1
        if self.unhungry_steps == 0:
            self.set_effect('hungry')
        for effect in self.effects:
            effect.affect(self.game)
        if self.health <= 0:
            print('DIED')
            # TODO ending
