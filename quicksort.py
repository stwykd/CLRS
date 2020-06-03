import random
def quicksort(arr): _quicksort(arr, 0, len(arr))

def _quicksort(arr, l, r):
    if r-l > 1:
        p = partition(arr, l, r)
        _quicksort(arr, l, p)
        _quicksort(arr, p+1, r)

def partition(arr, l, r):
    p_idx=random.randint(l,r-1)
    arr[l],arr[p_idx]=arr[p_idx],arr[l]
    p,i=arr[p_idx],l+1
    for j in range(l+1,r):
        if arr[j] < p:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[l],arr[i-1]=arr[i-1],arr[l]
    return i-1

def shuffle_sort_assert(a):
    random.shuffle(a)
    quicksort(a)
    assert a == sorted(a)

shuffle_sort_assert(range(10)) # positive values
shuffle_sort_assert(range(5,50000)) # large list of positive values
shuffle_sort_assert(range(-100,100,20)) # positive and negative values
shuffle_sort_assert(range(-200,-10,10)) # negative values
shuffle_sort_assert([]) # empty list
shuffle_sort_assert([3]) # one element
shuffle_sort_assert([1]*10) # duplicates
shuffle_sort_assert([float('inf')]*30+range(3)) # infinity comparisons
shuffle_sort_assert([0,0,0,2,-2]) # zero comparisons
