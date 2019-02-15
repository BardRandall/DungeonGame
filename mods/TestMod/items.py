from basics import BasicItem
from GUI import GUI


class ghost(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_own_image('mods/TestMod/ghost.png', 0, 0)
        self.used = False

    def do_nothing(self, variant, game):
        game.gui = None

    def callback(self, variant, game):
        if variant == 0:
            game.player.add_to_inventory(game.im.items_store['sword'])
        else:
            game.player.add_to_inventory(game.im.items_store['fabric_armour'])
        game.gui = None

    def take_item_event(self, game):
        if self.used:
            return False
        rose = game.im.items_store['rose']
        if rose in game.player.inventory.store:
            del game.player.inventory.store[game.player.inventory.store.index(rose)]
            game.gui = GUI(game).set_text('Выбери награду').set_choices(['Оружие', 'Доспехи'], self.callback)
            self.used = True
        else:
            game.gui = GUI(game).set_text('Принеси мне розу, и я дам тебе приз').set_choices(['ОК'], self.do_nothing)
        return False


class rose(BasicItem):

    def __init__(self):
        super().__init__()
        self.load_image(4, 12)

    def get_description(self):
        return 'Кажется, это роза приведения'
