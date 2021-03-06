from Constants import *
import pygame


class GUI:

    def __init__(self, game):
        self.game = game
        self.img = None
        self.text = ''
        self.choices = []
        self.font = pygame.font.Font(None, 16)
        self.buttons = []
        self.callback = self.do_nothing

    def do_nothing(self, *args):
        pass

    def set_img(self, img):
        self.img = img
        return self

    def set_text(self, text):
        self.text = text
        return self

    def set_choices(self, choices, callback):
        self.callback = callback
        for choice in choices:
            self.choices.append(self.font.render(choice, True, INVENTORY_FONT_COLOR))
        return self

    def render(self):
        symbol_rect = self.font.render('о', True, INVENTORY_FONT_COLOR).get_rect()
        max_length = (GUI_WIDTH - 2 * GUI_BORDER) // symbol_rect.width
        text = []
        height = 2 * GUI_BORDER + 2 * GUI_BUTTON_BORDER_WIDTH + GUI_BUTTON_INDENT + symbol_rect.height
        text_height = 0
        for i in range(0, len(self.text), max_length):
            if i + max_length >= len(self.text):
                txt = self.font.render(self.text[i:], True, INVENTORY_FONT_COLOR)
                text.append(txt)
                text_height += txt.get_rect().height
            else:
                txt = self.font.render(self.text[i:i + max_length], True, INVENTORY_FONT_COLOR)
                text.append(txt)
                text_height += txt.get_rect().height
        height += text_height
        pygame.draw.rect(self.game.screen, GUI_COLOR, (
            GUI_X,
            GUI_Y,
            GUI_WIDTH,
            height
        ), 0)
        for i in range(len(text)):
            self.game.screen.blit(
                text[i],
                (
                    GUI_BORDER + GUI_X,
                    GUI_BORDER + GUI_Y + i * text[i].get_rect().height
                )
            )
        filling = False
        if not self.buttons:
            filling = True
        last_symbols = 0
        for i in range(len(self.choices)):
            if filling:
                self.buttons.append((
                    GUI_X + GUI_BORDER + i * GUI_BUTTON_INDENT + last_symbols + i * GUI_BUTTON_INDENT,
                    GUI_Y + text_height + GUI_BUTTON_SPACE + symbol_rect.height,
                    2 * GUI_BUTTON_BORDER_WIDTH + self.choices[i].get_rect().width,
                    2 * GUI_BUTTON_BORDER_HEIGHT + self.choices[i].get_rect().height
                ))
            pygame.draw.rect(self.game.screen, GUI_BUTTON_COLOR, (
                GUI_X + GUI_BORDER + i * GUI_BUTTON_INDENT + last_symbols + i * GUI_BUTTON_INDENT,
                GUI_Y + text_height + GUI_BUTTON_SPACE + symbol_rect.height,
                2 * GUI_BUTTON_BORDER_WIDTH + self.choices[i].get_rect().width,
                2 * GUI_BUTTON_BORDER_HEIGHT + self.choices[i].get_rect().height
            ))
            self.game.screen.blit(
                self.choices[i],
                (
                    GUI_X + GUI_BORDER + i * GUI_BUTTON_INDENT +
                    last_symbols + i * GUI_BUTTON_INDENT + GUI_BUTTON_BORDER_HEIGHT,
                    GUI_Y + text_height + GUI_BUTTON_SPACE + symbol_rect.height + GUI_BUTTON_BORDER_HEIGHT
                )
            )
            last_symbols += self.choices[i].get_rect().width

    def click(self, i):
        self.callback(i, self.game)
        self.game.step()
        if self.game.player.show_inventory:
            self.game.player.inventory.choosed = None
            self.game.gui = None


class Inventory:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.store = []
        self.choosed = None

    def append(self, item):
        self.store.append(item)

    def render(self):
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
                if self.choosed is not None:
                    if type(self.choosed) == int and j == 0:
                        if (self.choosed == WEAPON and i == 0) or \
                                (self.choosed == ARMOUR and i == 1) or \
                                (self.choosed == RING1 and i == 2) or \
                                (self.choosed == RING2 and i == 3):
                            pygame.draw.rect(
                                self.screen,
                                INVENTORY_CHOOSE_COLOR,
                                (
                                    x,
                                    y,
                                    INVENTORY_CELL,
                                    INVENTORY_CELL
                                )
                            )
                            if i == 0:
                                if self.game.player.weapon is None:
                                    self.screen.blit(self.game.im.get_texture('weapon_shadow'), (x + 8, y + 8))
                                else:
                                    self.screen.blit(self.game.player.weapon.img, (x + 8, y + 8))
                            elif i == 1:
                                if self.game.player.armour is None:
                                    self.screen.blit(self.game.im.get_texture('armour_shadow'), (x + 8, y + 8))
                                else:
                                    self.screen.blit(self.game.player.armour.img, (x + 8, y + 8))
                            elif i == 2:
                                if self.game.player.ring1 is None:
                                    self.screen.blit(self.game.im.get_texture('ring_shadow'), (x + 8, y + 8))
                                else:
                                    self.screen.blit(self.game.player.ring1.img, (x + 8, y + 8))
                            elif i == 3:
                                if self.game.player.ring2 is None:
                                    self.screen.blit(self.game.im.get_texture('ring_shadow'), (x + 8, y + 8))
                                else:
                                    self.screen.blit(self.game.player.ring1.img, (x + 8, y + 8))
                            continue
                    if type(self.choosed) != int:
                        if self.choosed[0] == j and self.choosed[1] == i:
                            pygame.draw.rect(
                                self.screen,
                                INVENTORY_CHOOSE_COLOR,
                                (
                                    x,
                                    y,
                                    INVENTORY_CELL,
                                    INVENTORY_CELL
                                )
                            )
                            if item_index < len(self.store):
                                self.screen.blit(self.store[item_index].img, (x + 8, y + 8))
                                item_index += 1
                            continue
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
                if j == 0:
                    if i == 0:
                        if self.game.player.weapon is None:
                            self.screen.blit(self.game.im.get_texture('weapon_shadow'), (x + 8, y + 8))
                        else:
                            self.screen.blit(self.game.player.weapon.img, (x + 8, y + 8))
                    elif i == 1:
                        if self.game.player.armour is None:
                            self.screen.blit(self.game.im.get_texture('armour_shadow'), (x + 8, y + 8))
                        else:
                            self.screen.blit(self.game.player.armour.img, (x + 8, y + 8))
                    elif i == 2:
                        if self.game.player.ring1 is None:
                            self.screen.blit(self.game.im.get_texture('ring_shadow'), (x + 8, y + 8))
                        else:
                            self.screen.blit(self.game.player.ring1.img, (x + 8, y + 8))
                    elif i == 3:
                        if self.game.player.ring2 is None:
                            self.screen.blit(self.game.im.get_texture('ring_shadow'), (x + 8, y + 8))
                        else:
                            self.screen.blit(self.game.player.ring1.img, (x + 8, y + 8))
                    continue
                if item_index < len(self.store):
                    self.screen.blit(self.store[item_index].img, (x + 8, y + 8))
                    item_index += 1

    def click(self, i, j):
        if i * INVENTORY_COLS + j - 4 >= len(self.store):
            return
        if i == 0 and ((self.choosed == WEAPON and j == 0) or
                       (self.choosed == ARMOUR and j == 1) or
                       (self.choosed == RING1 and j == 2) or
                       (self.choosed == RING2 and j == 3)):
            self.choosed = None
            self.game.gui = None
            return
        if self.choosed is None or self.choosed != [i, j]:
            if i == 0:
                if j == 0:
                    self.choosed = WEAPON
                    item = self.game.player.weapon
                    if item is not None:
                        self.game.gui = GUI(self.game).set_text(item.get_description()).set_choices(
                            *item.get_choices(self.game))
                elif j == 1:
                    self.choosed = ARMOUR
                    item = self.game.player.armour
                    if item is not None:
                        self.game.gui = GUI(self.game).set_text(item.get_description()).set_choices(
                            *item.get_choices(self.game))
                elif j == 2:
                    self.choosed = RING1
                    item = self.game.player.ring1
                    if item is not None:
                        self.game.gui = GUI(self.game).set_text(item.get_description()).set_choices(
                            *item.get_choices(self.game))
                elif j == 3:
                    self.choosed = RING2
                    item = self.game.player.ring2
                    if item is not None:
                        self.game.gui = GUI(self.game).set_text(item.get_description()).set_choices(
                            *item.get_choices(self.game))
            else:
                self.choosed = [i, j]
                item = self.store[i * INVENTORY_COLS + j - 4]
                self.game.gui = GUI(self.game).set_text(item.get_description()).set_choices(
                    *item.get_choices(self.game))
        else:
            self.choosed = None
            self.game.gui = None

    def remove_item(self):
        if self.choosed is None:
            return
        return self.store.pop(self.choosed[0] * INVENTORY_COLS + self.choosed[1] - 4)

    def get_item(self):
        return self.store[self.choosed[0] * INVENTORY_COLS + self.choosed[1] - 4]

    def throw_item(self):
        if self.choosed is None:
            return
        player = self.game.player
        if self.game.im.summon_event(
                self.store[self.choosed[0] * INVENTORY_COLS + self.choosed[1] - 4].__class__.__name__,
                THROW_ITEM_EVENT, self.game):
            item = self.remove_item()
            self.game.level.spawn_item(item.__class__.__name__, player.cell_x, player.cell_y)
