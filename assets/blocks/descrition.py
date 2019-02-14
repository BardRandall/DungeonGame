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


class upstairs(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(7, 0, 0)

    def go_into_event(self, game):
        game.player.teleport_to_cell(0, 0)


class door(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(5, 0, 0)

    def go_into_event(self, game):
        pass

    def go_out_event(self, game):
        pass

    def get_img(self):
        return self.img
