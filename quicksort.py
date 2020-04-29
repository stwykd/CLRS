import random


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    smaller = [i for i in array if i < pivot]
    larger = [i for i in array if i > pivot]
    return quick_sort(smaller) + [i for i in array if i == pivot] + quick_sort(larger)