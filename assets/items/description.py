from basics import BasicItem, FoodItem, WeaponItem, ArmourItem, RingItem


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

    def get_damage(self):
        return 2


class sworld(WeaponItem):

    def __init__(self):
        super().__init__()
        self.load_image(2, 0)
        self.name = 'sworld'

    def get_description(self):
        return 'Меч: наносит от 2 до 4 единиц урона'

    def get_damage(self):
        return 2



class fabric_armour(ArmourItem):

    def __init__(self):
        super().__init__()
        self.load_image(0, 3)
        self.name = 'fabric_armour'

    def get_description(self):
        return 'Тканевый доспех. Обеспечивает простейшую защиту. Снижает урон на 30%'

    def get_defence(self):
        return 0.3


class bread(FoodItem):

    def __init__(self):
        super().__init__()
        self.load_image(4, 0)

    def get_description(self):
        return 'Сухой паек: дешево и сердито'


class magic_wend(WeaponItem):

    def __init__(self):
        super().__init__()
        self.load_image(3, 0)
        self.name = 'magic wade'

    def get_description(self):
        return 'волшебная Палочка: наносит от 1 до 5 единиц урона'


class standart_chest(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(3, 1)
        self.name = 'chest'

    def get_description(self):
        return 'Здесь спрятаны разные побрякушки'
