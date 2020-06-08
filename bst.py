class Node(object):
    def __init__(self, parent, k):
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        # Returns a reference to the node with key `k`
        if k == self.key:
            return self
        elif k < self.key:
            if not self.left:
                return None
            else:
                return self.left.find(k)
        else:
            if not self.right:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def next_larger(self):
        if self.right:
            return self.right.find_min()
        current = self
        while current.parent and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        if not node:
            return
        if node.key < self.key:
            if not self.left:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if not self.right:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        if not self.left or not self.right:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right:
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
        if not self.root:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def insert_values(self, l):
        for v in l:
            self.insert(v)

    def delete(self, k):
        node = self.find(k)
        if not node:
            return None
        if node is self.root:
            temp = Node(None, 0)
            temp.left = self.root
            self.root.parent = temp
            deleted = self.root.delete()
            self.root = temp.left
            if self.root:
                self.root.parent = None
            return deleted
        else:
            return node.delete()

    def delete_values(self, l):
        for v in l:
            self.delete(v)

    def next_larger(self, k):
        node = self.find(k)
        return node and node.next_larger()

    def inorder_tree_walk(self):
        def _inorder(x):
            if x:
                _inorder(x.left)
                nodes.append(x.key)
                _inorder(x.right)
        nodes = []
        _inorder(self.root)
        return nodes

tree = BST()
l = [7,5,9,1,6,10,13,-3,-7,-1,0,-12]
tree.insert_values(l)
assert tree.inorder_tree_walk() == sorted(l)

tree.delete(-3); l.remove(-3)
assert tree.inorder_tree_walk() == sorted(l)

to_delete = [-12,5,0]
tree.delete_values(to_delete)
for x in to_delete:
    l.remove(x)
assert tree.inorder_tree_walk() == sorted(l)

assert tree.find_min().key == min(l)
tree.delete(tree.find_min().key); l.remove(min(l))
assert tree.find_min().key == min(l)

to_find = [10,1,3]
for x in to_find:
    assert bool(tree.find(x)) == (x in l)
