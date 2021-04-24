class Counters:
    """ Manages a set of peg counters """
    def __init__(self):
        self.__counters = {}

    @property
    def number(self):
        return len(self.__counters)

    def count(self, name):
        return self.__counters.get(name, 0)

    def increment(self, name):
        value = self.count(name);
        self.__counters[name] = value + 1
