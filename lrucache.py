class LRUCache:

    # @param capcacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict

    # @return an integer
    def get(self, key):
        if not self.cache[key]:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last = False)
        self.cache[key] = value
