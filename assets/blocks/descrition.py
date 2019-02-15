from basics import BasicBlock


class brick_wall(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(0, 1, 0)

    def can_go(self):
        return False


class brick_floor(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(1, 0, 0)


class upstairs(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(7, 0, 0)

    def go_into_event(self, game):
        game.player.teleport_to_cell(0, 0)


class wood_door(BasicBlock):  # костыль!!!

    def __init__(self):
        super().__init__()
        self.load_image(5, 0, 0)

    def go_into_event(self, game):
        game.level.is_open_door = True

    def go_out_event(self, game):
        game.level.is_open_door = False


class open_door(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(6, 0, 0)


class opened_door(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(6, 0, 0)


class pillar(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(12, 2, 0)


class wood_monument(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(4, 2, 0)


class moody_floor(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(8, 2, 0)


class thrd_brick_floor(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(0, 15, 0)


class pit(BasicBlock):
    def __init__(self):
        super().__init__()
        self.load_image(11, 2, 0)


class stair_down(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(8, 0, 0)

    def go_into_event(self, game):
        game.player.teleport_to_cell(0, 0)


class wood_floor(BasicBlock):

    def __init__(self):
        super().__init__()
        self.load_image(1, 0, 0)


class steel_locked_door(BasicBlock):
    def __init__(self):
        super().__init__()
        self.load_image(5, 0, 0)

    def go_into_event(self, game):
        game.level.is_open_door = True

    def go_out_event(self, game):
        game.level.is_open_door = False
