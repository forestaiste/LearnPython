import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """add element from iterable objects"""

    @abc.abstractmethod
    def pick(self):
        """delete element randomly, and return it"""
        
    def loaded(self):
        return bool(self.inspcet())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        self.load(items)
        return tuple(sorted(items))


