from Constants import *
import pygame


class GUI:

    def __init__(self, game):
        self.game = game
        self.img = None
        self.text = ''
        self.choices = []
        self.font = pygame.font.Font(None, 16)

    def set_img(self, img):
        self.img = img
        return self

    def set_text(self, text):
        self.text = text
        return self

    def set_choices(self, choices):
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
                txt = self.font.render(self.text[i:i+max_length], True, INVENTORY_FONT_COLOR)
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
        last_symbols = 0
        for i in range(len(self.choices)):
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


class Inventory:

    def __init__(self, game):
        self.game = game
        self.store = []

    def append(self, item):
        self.store.append(item)

    def render(self):
        pass
