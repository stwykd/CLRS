# merge sort
def merge(a1, a2):
    i, j, a = 0, 0, []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a.append(a1[i])
            i += 1
        else:
            a.append(a2[j])
            j += 1
    a.extend(a1[i:] + a2[j:])
    return a
def merge_sort(a):
    if len(a) == 1:
        return a
    left = merge_sort(a[:len(a) / 2])
    right = merge_sort(a[len(a) / 2:])
    return merge(left, right)

assert merge([1, 2, 3], [4, 5, 6]) == range(1, 7)  # same size
assert merge([1, 2, 3, 4], [5, 6]) == range(1, 7)  # diff size
assert merge([], [1, 2, 3, 4]) == [1, 2, 3, 4]  # one empty
assert merge([1, 2, 3, 4], []) == [1, 2, 3, 4]
assert merge([1, 2, 4, 5], [3]) == [1, 2, 3, 4, 5]  # one element
assert merge([3], [4]) == [3, 4]
assert merge([1, 3], [2 ** 5, 2 ** 6, 2 ** 7]) == [1, 3, 2 ** 5, 2 ** 6, 2 ** 7]  # stress test
assert merge([-3, -2, 1], [0]) == [-3, -2, 0, 1]  # negatives
assert merge([3, 3, 3], [3, 3]) == [3] * 5  # duplicates
assert merge([1, 1, 1], [4, 4, 4, 4]) == [1] * 3 + [4] * 4
assert merge_sort([6, 5, 4, 3, 2, 1]) == range(1, 7)  # reversed-order
assert merge_sort([3, -7, 1, 0, -1, -5]) == [-7, -5, -1, 0, 1, 3]  # negatives
assert merge_sort([3, 3, 3, 3]) == [3, 3, 3, 3]  # duplicates
assert merge_sort(range(50)[::-1] * 2 ** 10)  # stress test


# quick sort
import random
def quicksort(arr): _quicksort(arr, 0, len(arr))
def _quicksort(arr, l, r):
    if r - l > 1:
        p = partition(arr, l, r)
        _quicksort(arr, l, p)
        _quicksort(arr, p + 1, r)
def partition(arr, l, r):
    p_idx = random.randint(l, r - 1)
    p, i = arr[p_idx], l + 1
    arr[l], arr[p_idx] = arr[p_idx], arr[l]
    for j in range(l + 1, r):
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    return i - 1

def shuffle_sort_assert(a):
    random.shuffle(a)
    quicksort(a)
    assert a == sorted(a)
shuffle_sort_assert(range(10))  # positive values
shuffle_sort_assert(range(5, 50000))  # large list of positive values
shuffle_sort_assert(range(-100, 100, 20))  # positive and negative values
shuffle_sort_assert(range(-200, -10, 10))  # negative values
shuffle_sort_assert([])  # empty list
shuffle_sort_assert([3])  # one element
shuffle_sort_assert([1] * 10)  # duplicates
shuffle_sort_assert([float('inf')] * 30 + range(3))  # infinity comparisons
shuffle_sort_assert([0, 0, 0, 2, -2])  # zero comparisons


# counting sort
def counting_sort(a):
    counts, sorted_ = [0]*(max(a)+1), []
    for k in a:
        counts[k] += 1
    for i in range(len(counts)):
        sorted_.extend([i]*counts[i])
    return sorted_


# insertion sort
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


# bubble sort
def bubble_sort(arr):
    is_sorted = False
    last_unsorted = len(arr) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(0, last_unsorted):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        last_unsorted -= 1
