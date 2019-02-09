import assets.blocks.descrition as blocks
import assets.items.description as items


class BlockManager:

    def __init__(self):
        self.blocks_store = {}
        for block in dir(blocks)[9:]:
            self.blocks_store[block] = eval('blocks.{}()'.format(block))

    def get_texture(self, name):
        return self.blocks_store[name].img


class ItemManager:

    def __init__(self):
        self.items_store = {}
        for item in dir(items)[9:]:
            self.items_store[item] = eval('items.{}()'.format(item))

    def get_texture(self, name):
        return self.items_store[name].img
