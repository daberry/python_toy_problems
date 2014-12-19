class Vertex(object):
    def __init__(self, node):
        self.value = node
        self.list = []

class Graph(object):
    def __init__(self):
        self.collection = {}

    def add_node(self, new_node, to_node):
        counter = 0
        new_vertex = Vertex(new_node)
        self.collection[new_node] = new_vertex
        if to_node != None:
            self.add_edge(new_node, to_node)
        else:
            for node in self.collection:
                counter += 1
            if counter == 2:
                for node in self.collection:
                    if node != new_node:
                        node1 = node
                self.add_edge(new_node, node1)

    def contains(self, node):
        for key in self.collection:
            if key == node: return True
        return False

    def remove_node(self, node):
        removed_vertex = self.collection[node]
        if removed_vertex != None:
            for i in range(0, len(removed_vertex.list)):
                self.remove_edge(node, removed_vertex.list[i])
            delete self.collection[node]
