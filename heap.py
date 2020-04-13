class Heap:
    '''implementation of a max heap as an array,
    visualized as a nearly complete binary tree'''
    def __init__(self, arr):
        self.A = arr
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.A)//2, 0, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        l = i << 1
        r = (i << 1) + 1
        if l <= len(self.A) and self.A[l-1] > self.A[i-1]:
            largest = l
        else:
            largest = i
        if r <= len(self.A) and self.A[r-1] > self.A[largest-1]:
            largest = r
        if largest != i:
            temp = self.A[largest-1]
            self.A[largest-1] = self.A[i-1]
            self.A[i-1] = temp
            self.max_heapify(largest)

h = Heap([1, 5, 4, 6, 7, 8, 6, 4, 3, 2, 1, 5, 2])
print h.A