class Node:
    def __init__(self):
        self.children = []
        self.is_complete_word = False
        self.size = 0

    def get_node(self, c):
        return self.children[c - 'a']

    def set_node(self, c, node):
        self.children[c - 'a'] = node

    def add(self, s, index):
        self.size += 1
        if index is (len(s)):
            return
        current = s[index]
        child = self.get_node(current)
        if child is None:
            child = Node()
            self.set_node(current, child)
        child.add(s, index + 1)

    def find_count(self, s, index):
        if index is len(s):
            return self.size
        child = self.get_node(s[index])
        if child is None:
            return 0
        return child.find_count(s, index + 1)
