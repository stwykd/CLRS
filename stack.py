class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            return -1

        return self.top.data

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return -1

        data = self.top.data
        self.top = self.top.next
        return data
