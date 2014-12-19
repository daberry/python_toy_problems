class Node(object):
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def createNode(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node 
        self.tail = node
        self.length += 1

    def head(self):
        return self.head

    def tail(self):
        return self.tail

    def reverse(self, node=None):
        if node == None : return
        head = node
        tail = node.next
        self.reverse(tail)
