def quick_sort(array):
    quick_sort(array, 0, len(array) - 1)


def quick_sort(array, left, right):
    if left >= right:
        return
    pivot = array[(left + right) / 2]
    index = partition(array, left, right, pivot)
    quick_sort(array, left, index - 1)
    quick_sort(array, index, right)


def swap(array, left, right):
    tmp = array[left]
    array[left] = array[right]
    array[right] = tmp


def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right += 1
        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1
    return left
