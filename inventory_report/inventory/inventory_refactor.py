from collections.abc import Iterator


class InventoryRefactor(Iterator):

    def __init__(self, value, instance):
        self.data = value
        self.instance = self.class_file(instance)

    def __next__(self):
        if self.index < self.value:
            index = self.index
            self.index = self.index + 1
            return index
        else:
            raise StopIteration()

    def class_file(instance):
        pass

    def verify_instance(self, instance):
        return isinstance(instance, type)
