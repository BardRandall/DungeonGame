from Constants import *
from PIL import Image
import pygame.image as pim
import pygame


class Player:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        self.absolute_x, self.absolute_y = 0, 0
        self.cell_x = 0
        self.cell_y = 0
        self.img = self._load_image(0, 0)

        self.wearing = 0
        self.moving_animation = []
        for i in [0, 2, 3, 4, 5, 6, 7, 0, 0]:
            self.moving_animation.append(self._load_image(i, self.wearing))
        self.facing = RIGHT
        self.moving = None
        self.moving_state = 0
        self.inv_choose = None

        self.inventory = []

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
        if len(self.inventory) < MAX_ITEMS:
            if type(item) != str:
                self.inventory.append(item)
            else:
                self.inventory.append(self.game.im.items_store[item])
            return True
        return False

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

    def render_inventory(self):
        pygame.draw.rect(
                             self.screen,
                             INVENTORY_BORDER_COLOR,
                             (INVENTORY_X,
                              INVENTORY_Y,
                              INVENTORY_WIDTH,
                              INVENTORY_HEIGHT)
        )
        font = pygame.font.Font(None, 25)
        text = font.render(INVENTORY_TITLE, True, INVENTORY_FONT_COLOR)
        text_width = 2 * INVENTORY_LOW_SPACE + INVENTORY_CELL * INVENTORY_COLS + (INVENTORY_COLS - 1) * INVENTORY_SPACES
        text_rect = text.get_rect()
        self.screen.blit(text, (
                                (text_width - text_rect.width) // 2 + INVENTORY_X,
                                (INVENTORY_MAX_SPACE - text_rect.height) // 2 + INVENTORY_Y
                                )
                         )
        item_index = 0
        for j in range(INVENTORY_ROWS):
            for i in range(INVENTORY_COLS):
                x = INVENTORY_X + INVENTORY_LOW_SPACE + (INVENTORY_CELL + INVENTORY_SPACES) * i
                y = INVENTORY_Y + INVENTORY_MAX_SPACE + (INVENTORY_CELL + INVENTORY_SPACES) * j
                pygame.draw.rect(
                    self.screen,
                    INVENTORY_COLOR,
                    (
                        x,
                        y,
                        INVENTORY_CELL,
                        INVENTORY_CELL
                    )
                )
                if item_index < len(self.inventory):
                    self.screen.blit(self.inventory[item_index].img, (x + 8, y + 8))
                    item_index += 1

    def click_inventory(self, i, j):
        self.inv_choose = (i, j)

