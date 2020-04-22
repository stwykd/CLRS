class Heap:
    # Implementation of a max heap as an array,
    # visualized as a nearly complete binary tree
    def __init__(self, arr):
        self.arr = arr
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.arr)//2, 0, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        l = i << 1
        r = (i << 1) + 1
        if l <= len(self.arr) and self.arr[l-1] > self.arr[i-1]:
            largest = l
        else:
            largest = i
        if r <= len(self.arr) and self.arr[r-1] > self.arr[largest-1]:
            largest = r
        if largest != i:
            temp = self.arr[largest-1]
            self.arr[largest-1] = self.arr[i-1]
            self.arr[i-1] = temp
            self.max_heapify(largest)

    def heap_sort(self):
        l = list()
        for i in range(len(self.arr)-1, -1, -1):
            l.append(self.arr[0])
            self.arr[0] = self.arr[i]
            del self.arr[i]
            self.max_heapify(1)
        print l

h = Heap([1, 5, 4, 6, 7, 8, 6, 4, 3, 2, 1, 5, 2])
print h.arr
h.heap_sort()
