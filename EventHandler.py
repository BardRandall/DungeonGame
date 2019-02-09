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
        self._handle_pressed()

    def _handle_pressed(self):
        if self.pressed == pygame.K_UP:
            self.game.player.step(UP)
        elif self.pressed == pygame.K_RIGHT:
            self.game.player.step(RIGHT)
        elif self.pressed == pygame.K_DOWN:
            self.game.player.step(DOWN)
        elif self.pressed == pygame.K_LEFT:
            self.game.player.step(LEFT)

    def _handle_keydown(self, event):
        self.pressed = event.key

    def _handle_keyup(self, event):
        if event.key == self.pressed:
            self.pressed = None
