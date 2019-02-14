import assets.blocks.descrition as blocks
import assets.items.description as items
import assets.effects.description as effects
from basics import *


class BlockManager:

    def __init__(self):
        self.blocks_store = {}
        for block in dir(blocks)[9:]:
            self.blocks_store[block] = eval('blocks.{}()'.format(block))

    def get_texture(self, name):
        return self.blocks_store[name].get_img()

    def summon_event(self, name, event, game):
        obj = self.blocks_store[name]
        if event == CAN_GO_EVENT:
            return obj.can_go()
        elif event == GO_INTO_EVENT:
            return obj.go_into_event(game)
        elif event == GO_OUT_EVENT:
            return obj.go_out_event(game)


class ItemManager:

    def __init__(self):
        self.items_store = {}
        for item in dir(items)[10:]:
            self.items_store[item] = eval('items.{}()'.format(item))

    def get_texture(self, name):
        return self.items_store[name].img

    def summon_event(self, name, event, game):
        obj = self.items_store[name]
        if event == TAKE_ITEM_EVENT:
            return obj.take_item_event(game)
        elif event == THROW_ITEM_EVENT:
            return obj.throw_item_event(game)


class EffectManager:

    def __init__(self):
        self.effects_store = {}
        for effect in dir(effects)[10:]:
            self.effects_store[effect] = eval('effects.{}()'.format(effect))

    def find(self, name):
        return self.effects_store[name]
