import pygame
from Constants import *
from game import Game

pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
timer = pygame.time.Clock()
pygame.display.set_caption('Dungeon Hunter')

game = Game(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            game.send_event(event)
    screen.fill((0, 0, 0))
    game.update()
    game.render()
    pygame.display.flip()
    timer.tick(FPS)

pygame.quit()
