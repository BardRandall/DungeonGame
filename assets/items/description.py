from basics import BasicItem, FoodItem


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

    def get_description(self):
        return 'Меч: наносит от 2 до 4 единиц урона'


class packed_lunch(FoodItem):

    def __init__(self):
        super().__init__()
        self.load_image(4, 0)

    def get_description(self):
        return 'Сухой паек: дешево и сердито'
