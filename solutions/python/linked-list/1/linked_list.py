class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succ = succeeding
        self.pred = previous
class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
    def __len__(self):
        return self.length
    def __iter__(self):
        n = self.head
        while n is not None:
            yield n.value
            n = n.succ
    def push(self, value):
        n = Node(value)
        n.pred = self.tail
        if self.tail is None:
            self.head = n
        else:
            self.tail.succ = n
        self.tail = n
        self.length += 1
    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        n = self.tail
        self.tail = n.pred
        if self.tail is None:
            self.head = None
        else:
            self.tail.succ = None
        self.length -= 1
        return n.value
    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        n = self.head
        self.head = n.succ
        if self.head is None:
            self.tail = None
        else:
            self.head.pred = None
        self.length -= 1
        return n.value
    def unshift(self, value):
        n = Node(value)
        n.succ = self.head
        if self.head is None:
            self.tail = n
        else:
            self.head.pred = n
        self.head = n
        self.length += 1
    def delete(self, value):
        n = self.head
        while n is not None:
            if n.value == value:
                break
            n = n.succ
        else:
            raise ValueError("Value not found")
        if n.pred is not None:
            n.pred.succ = n.succ
        if n.succ is not None:
            n.succ.pred = n.pred
        if n == self.head:
            self.head = n.succ
        if n == self.tail:
            self.tail = n.pred
        self.length -= 1