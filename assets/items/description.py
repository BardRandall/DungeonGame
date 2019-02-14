from basics import BasicItem, FoodItem, WeaponItem


def do_nothing(*args):
    pass


# For inventory
class weapon_shadow(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(5, 0)

    def get_description(self):
        return 'Место для оружия'

    def get_choices(self, game):
        return ['Закрыть'], do_nothing


class armour_shadow(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(6, 0)

    def get_description(self):
        return 'Место для брони'

    def get_choices(self, game):
        return ['Закрыть'], do_nothing


class ring_shadow(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(7, 0)

    def get_description(self):
        return 'Место для кольца'

    def get_choices(self, game):
        return ['Закрыть'], do_nothing


class skeleton(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(0, 0)

    def take_item_event(self, game):
        game.player.add_to_inventory('packed_lunch')
        return False


class sword(WeaponItem):

    def __init__(self):
        super().__init__()
        self.load_image(2, 0)
        self.name = 'sword'

    def get_description(self):
        return 'Меч: наносит от 2 до 4 единиц урона'


class packed_lunch(FoodItem):

    def __init__(self):
        super().__init__()
        self.load_image(4, 0)

    def get_description(self):
        return 'Сухой паек: дешево и сердито'
