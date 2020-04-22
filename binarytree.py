class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value is self.data:
            return True

        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)

        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()

        print self.data,

        if self.right is not None:
            self.right.print_in_order()
