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
        self.is_open_door = False
        self.game = game
        with open(LEVELS_DIR + filename) as f:
            self.data = json.load(f)
        self.screen = screen
        self.start_x = WIDTH // 2 - self.data['width'] * CELL_SIZE // 2
        self.start_y = HEIGHT // 2 - self.data['height'] * CELL_SIZE // 2
        field = self.data['board']
        self.board = []
        for i in range(len(field)):
            temp = []
            for j in range(len(field[i])):
                cell = Cell(i, j, field[i][j]['block'])
                if 'items' in field[i][j]:
                    cell.set_items(field[i][j]['items'])
                if 'mobs' in field[i][j]:
                    for mob in field[i][j]['mobs']:
                        mob = eval('self.game.mm.mobs_store["{0}"](self.game, {1})'.format(mob['mob'], mob['data']))
                        mob.teleport_to_cell(i, j, self.start_x, self.start_y)
                        game.mobs.append(mob)
                temp.append(cell)
            self.board.append(temp[:])
        player_x, player_y = self.data['start_pos']['x'], self.data['start_pos']['y']
        game.player.teleport_to_cell(player_x, player_y, self.start_x, self.start_y)

    def update(self):
        pass

    def spawn_item(self, item, x, y):
        self.board[x][y].add_item({'item': item, 'data': {}})

    def render(self):
        player = self.game.player
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                cell = self.board[i][j]
                if cell.block is None:
                    continue
                if self.is_open_door and i == player.cell_x and j == player.cell_y:
                    texture = self.bm.get_texture('open_door')
                else:
                    texture = self.bm.get_texture(cell.block)
                self.screen.blit(texture,
                                 (self.start_x + i * CELL_SIZE,
                                  self.start_y + j * CELL_SIZE))
                if cell.items:
                    for item in cell.items:
                        self.screen.blit(self.im.get_texture(item['item']),
                                 (self.start_x + i * CELL_SIZE,
                                  self.start_y + j * CELL_SIZE))
