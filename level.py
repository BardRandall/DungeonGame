import json
from Constants import *


class Cell:

    def __init__(self, x, y, block):
        self.x = x
        self.y = y
        self.block = block
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def set_items(self, items):
        self.items = items[:]
        return self


class Level:

    def __init__(self, filename, screen, game):
        self.bm = game.bm
        self.im = game.im
        with open(LEVELS_DIR + filename) as f:
            self.data = json.load(f)
        self.screen = screen
        field = self.data['board']
        self.board = []
        for i in range(len(field)):
            temp = []
            for j in range(len(field[i])):
                cell = Cell(i, j, field[i][j]['block'])
                if 'items' in field[i][j]:
                    cell.set_items(field[i][j]['items'])
                if 'mobs' in field[i][j]:
                    game.mobs = field[i][j]['mobs'][:]
                temp.append(cell)
            self.board.append(temp[:])
        self.start_x = WIDTH // 2 - self.data['width'] * CELL_SIZE // 2
        self.start_y = HEIGHT // 2 - self.data['height'] * CELL_SIZE // 2
        player_x, player_y = self.data['start_pos']['x'], self.data['start_pos']['y']
        game.player.teleport_to_cell(player_x, player_y, self.start_x, self.start_y)

    def update(self):
        pass

    def render(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                cell = self.board[i][j]
                self.screen.blit(self.bm.get_texture(cell.block),
                                 (self.start_x + i * CELL_SIZE,
                                  self.start_y + j * CELL_SIZE))
                if cell.items:
                    for item in cell.items:
                        self.screen.blit(self.im.get_texture(item['item']),
                                 (self.start_x + i * CELL_SIZE,
                                  self.start_y + j * CELL_SIZE))
