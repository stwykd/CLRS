class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head

    def peek(self):
        if self.head:
            return self.head.value

    def add(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
        self.tail = node

        if not self.head:
            self.head = node

    def remove(self):
        value = self.head.value
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return value

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return ' '.join(map(str, list(self)))


q = Queue()
q.add(0)
q.add(1)
q.add(2)
q.add(3)
assert list(q) == range(4)

assert q.remove() == 0
assert q.remove() == 1
assert q.peek() == 2
assert list(q) == [2, 3]

q.remove()
q.remove()
assert q.is_empty()
