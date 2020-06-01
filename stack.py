class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        return self.top.value if self.top else None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value

    def clear(self):
        self.top = None

    def __iter__(self):
        current = self.top
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return ' '.join(map(str, list(self)))

s = Stack()
s.push(3)
s.push(2)
s.push(1)
s.push(0)
assert list(s) == list(range(4))
assert s.pop() == 0
assert s.pop() == 1
assert list(s) == [2,3]

s.clear()
assert list(s) == []
assert s.is_empty()

assert s.pop() == None

s.push(2)
assert s.peek() == 2
