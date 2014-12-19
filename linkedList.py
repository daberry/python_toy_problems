class LinkedList:

    def __init__(self):
        self.data = {}
        self.head = None
        self.tail = None

    def addToTail(value):
        node = Node(value)
        if self.head = None:
            self.head = node
            self.tail = self.head
        else:
            self.head.next = node
            self.tail = self.tail.next
            self.tail.next = value

    def removeHead():
        if self.head != None:
            current = self.head.next
            self.head = self.head.next
            return current.value

    def contains(target):
        if self.head != None:
            first = self.head
            while first.value != target:
                if first == self.tail:
                    return False
                first = first.next
        return True

class Node:

    def __init__(self, value=None):
        self.node = {}
        self.value = value
        self.next = None
