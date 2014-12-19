class Tree(object):

    def __init__(self, value):
        self.value = value
        self.children = []

    def DFSelect(self, filter):
        result = []
        def traverse(self):
            if len(self.children) is not 0:
                for child in self.children:
                    child.DFSelect(filter)
            else:
                if filter(self):
                    result.append(self)
                return
        return result
