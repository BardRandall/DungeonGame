from basics import BasicItem


class skeleton(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(0, 0)

    def take_item_event(self, game):
        return False


class sword(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(2, 0)
