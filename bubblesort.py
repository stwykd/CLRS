def bubble_sort(array):
    is_sorted = False
    last_unsorted = len(array) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(0, last_unsorted):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                is_sorted = False
        last_unsorted -= 1


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
