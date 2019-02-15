from basics import BasicMob


class mouse(BasicMob):

    def __init__(self, game, data):
        super().__init__(game)
        self.data = data
        self.img = self.load_image(0, 0, 'mouse.png')
        self.load_animation([3, 4, 5, 6, 7, 8, 9, 10, 0, 0], 0, 'mouse.png')
