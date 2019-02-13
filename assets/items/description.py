from basics import BasicItem


class skeleton(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(0, 0)

    def take_item_event(self, game):
        game.player.add_to_inventory('packed_lunch')
        return False


class sword(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(2, 0)


class packed_lunch(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(4, 0)
