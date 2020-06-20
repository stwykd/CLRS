# Full binary tree with at least n leaf nodes
# kth leaf node stores the value of item k
# Each internal node stores the sum of values of its children

# Choose the minimal set of nodes whose sum gives the desired value
# – at most 1 node is chosen at each level so that the total
#   number of nodes we look at is log2 n
# – This can be done in O(log n) time

class Fenwick():
    def __init__(self, l=[]):
        self.N = len(l)
        self.BIT = [0 for i in xrange(self.N)]
        for i in xrange(1,self.N+1):
            self.update(i, l[i-1])


    def update(self, i, x):
        # Add x to the ith position
        while i <= self.N:
            # ... Working with an 1-based array
            self.BIT[i-1] += x
            i += i & (-i)

    def query(self, i):
         # Find the ith prefix sum
        s = 0
        while i > 0:
            s += self.BIT[i-1]
            i -= i & (-i)
        return s

# Extension: Make the Sum() function work for any interval
# – ... not just ones that start from item 1
