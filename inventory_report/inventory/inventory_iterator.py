from collections.abc import Iterable


class InventoryIterator(Iterable):
    def __init__(self, value):
        self.importer = value

    def __iter__(self):
        return Iterable(self.value)
