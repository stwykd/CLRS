# Each object is name with an integer from 0 to N-1
# Connection are:
#   - Reflexive: p is connected to p
#   - Symmetric: if p is connected to q, then q is connected to p
#   - Transitive: if p is connected to q and q is connected to r,
#                 then p is connected to r


class QuickFind:
    # Connected components is the maximal set of objects that
    # are mutually connected

    def __init__(self, n): # O(n)
        # id: p and q are connected iff they have the same id
        self.id = range(n)


    def find(self, p, q): # O(1)
    # Is there a path connecting p and q
    # To do this, check if p and q belong to the same component
        return self.id[p] == self.id[q]

    def union(self, p, q): # O(n)
    # Add connection between p and q
    # To do this, replace components containing p and q, with their union
        pid, qid = self.id[p], self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid: self.id[i] = qid



class QuickUnion:
    def __init__(self, n): # O(n)
        # `id` now represents a set of trees (or a forest)
        # Each entry in `id` is a reference to its parent in the tree
        # Roots in each tree point to themselves
        self.id = range(n)

    def root(self, i):
        while i != self.id[i]: i = self.id[i]
        return i

    def find(self, p, q): # O(n)
        # Check if p and q have the same root
        return root(p) == root(q)

    def union(self, p, q): # O(n)
        # Set the id of p's root to the id of q's root
        self.id[root(p)] = root(q)

# Improvements:
# - weighted union
# - path compression


qf = QuickFind(10)
pairs = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9), (5, 0),
         (7, 2), (6, 1), (1, 0), (6, 7)]

for p,q in pairs:
    if not qf.find(p, q):
        qf.union(p, q)
