class Heap:
    def __init__(self, arr):
        self.arr = arr[:]
        self.build_max_heap()

    def insert(self, v):
        self.arr.append(v)
        self.build_max_heap()

    def max(self):
        return self.arr[0]

    def extract_max(self):
        highest = self.arr.pop(0)
        self.build_max_heap()
        return highest

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
            l.append(self.extract_max())
            self.max_heapify(1)
        return l

l = [1, 5, 4, 6, 7, 8, 6, 4, 3, 2, 1, 5, 2]
h = Heap(l)
assert h.heap_sort() == sorted(l)[::-1]
