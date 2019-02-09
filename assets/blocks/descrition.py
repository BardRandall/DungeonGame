from basics import BasicBlock


class brick_wall(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(0, 1, 0)

    def can_go(self):
        return False


class stone_floor(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(1, 0, 0)
