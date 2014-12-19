import set

class Set(set.Set):                 # this set class extends set.Set
    def __init__(self, value = []):
        self.data = {}              # manages a local dict
        self.concat(value)          # hashing: linear search times

    def intersect(self, other):
        result = {}
        for x in other:             # other: another sequence or Set
            if x in self.data:      # use hashtable lookup
                result[x] = None
        return Set(result.keys())   # a new dict-based Set

    def union(self, other):
        result = {}
        for x in other:             
            result[x] = None        
        for x in self.data.keys():
            result[x] = None
        return Set(result.keys())

    def concat(self, value):
        for x in value: self.data[x] = None

    # inherit and, or, and len properties
    def __getitem__(self, index):
        return list(self.data.keys())[index]

    def __repr__(self):
        return '<Set:%r>' % list(self.data.keys())
