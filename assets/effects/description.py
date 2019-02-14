from basics import BasicEffect
from Constants import UNHUNGRY_STEPS


class hungry(BasicEffect):

    def __init__(self):
        super().__init__()
        self.name = 'Голод'

    def affect(self, game):
        game.player.health -= 1
        game.player.unhungry_steps = UNHUNGRY_STEPS
