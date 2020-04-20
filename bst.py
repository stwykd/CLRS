class Node(object):

    def __init__(self, parent, k):
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

    def __str__(self):
        return str(self.key)


class BST(object):

    def __init__(self):
        self.root = None

    def find(self, k):
        return self.root and self.root.find(k)

    def find_min(self):
        return self.root and self.root.find_min()

    def insert(self, k):
        node = Node(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def delete(self, k):
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            temp = Node(None, 0)
            temp.left = self.root
            self.root.parent = temp
            deleted = self.root.delete()
            self.root = temp.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()

    def next_larger(self, k):
        node = self.find(k)
        return node and node.next_larger()

    def __str__(self):
        l = list()
        m = self.find_min().key
        l.append(m)
        while self.next_larger(m):
            l.append(self.next_larger(m).key)
            m = self.next_larger(m).key
        return ' '.join(map(str, l))


tree = BST()
tree.insert(7)
tree.insert(5)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(10)
tree.insert(13)
tree.insert(-3)
tree.insert(-7)
tree.insert(-1)
tree.insert(0)
tree.insert(-12)
print tree
tree.delete(-3)
print tree
tree.delete(-12)
tree.delete(5)
tree.delete(0)
print tree
print tree.find_min()
tree.delete(-7)
print tree.find_min()
print tree.find(10)