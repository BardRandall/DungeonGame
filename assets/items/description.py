from basics import BasicItem


class skeleton(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(0, 0)


class sword(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(2, 0)
