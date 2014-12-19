class BinarySearchTree(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left !== None:
                self.left.value = value
            else:
                self.left = BinarySearchTree(value)
                self.left.parent = self
        else:
            if self.right !== None:
                self.right.value = value
            else:
                self.right = BinarySearchTree(value)
                self.right.parent = self

    def contains(self, value):
        if self.value == value: return True
        if self.left !== None:
            self.left.contains(value)
        if self.right !== None:
            self.right.contains(value)
        return False

    def remove_from_parent(self):
        if self.parent !== None:
            parent_node = self.parent
            if parent_node.left == self:
                parent_node.left = None
            else:
                parent_node.right = None
        self.parent = None

    def depth_first_search(self):
        if self == None: return
        if self.left:
            self.left.depth_first_search()
        if self.right:
            self.right.depth_first_search()

    def breadth_first_search(self):
        if self == None: return
        queue = Queue()
        queue.enqueue(self)
        while len(queue) > 0:
            current = queue.dequeue()
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
