import pygame
from Constants import *


class EventHandler:

    def __init__(self, game):
        self.game = game
        self.pressed = None

    def handle(self, event):
        if event is None:
            self._handle_pressed()
            return
        if event.type == pygame.KEYDOWN:
            self._handle_keydown(event)
        if event.type == pygame.KEYUP:
            self._handle_keyup(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self._handle_mouse(event)
        self._handle_pressed()

    def _handle_mouse(self, event):
        if not self.game.show_inventory:
            return
        for j in range(INVENTORY_ROWS):
            for i in range(INVENTORY_COLS):
                x = INVENTORY_X + INVENTORY_LOW_SPACE + (INVENTORY_CELL + INVENTORY_SPACES) * i
                y = INVENTORY_Y + INVENTORY_MAX_SPACE + (INVENTORY_CELL + INVENTORY_SPACES) * j
                if x <= event.pos[0] <= x + INVENTORY_CELL and y <= event.pos[1] <= y + INVENTORY_CELL:
                    self.game.player.click_inventory(i, j)

    def _handle_pressed(self):
        if self.pressed == UP_KEY:
            self.game.step(UP)
        elif self.pressed == RIGHT_KEY:
            self.game.step(RIGHT)
        elif self.pressed == DOWN_KEY:
            self.game.step(DOWN)
        elif self.pressed == LEFT_KEY:
            self.game.step(LEFT)

    def _handle_keydown(self, event):
        if event.key == INVENTORY_KEY:
            self.game.show_inventory = not self.game.show_inventory
            return
        if not self.game.show_inventory:
            self.pressed = event.key

    def _handle_keyup(self, event):
        if event.key == self.pressed:
            self.pressed = None
