from basics import BasicEffect


class hungry(BasicEffect):

    def __init__(self):
        super().__init__()
        self.name = 'Голод'

    def affect(self, game):
        game.player.health -= 1
