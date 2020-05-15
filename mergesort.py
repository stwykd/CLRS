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

assert merge([1,2,3],[4,5,6]) == range(1,7) # same size
assert merge([1,2,3,4],[5,6]) == range(1,7) # diff size
assert merge([],[1,2,3,4]) == [1,2,3,4] # one empty
assert merge([1,2,3,4],[]) == [1,2,3,4]
assert merge([1,2,4,5],[3]) == [1,2,3,4,5] # one element
assert merge([3],[4]) == [3,4]
assert merge([1,3],[2**5,2**6,2**7]) == [1,3,2**5,2**6,2**7] # stress test
assert merge([-3,-2,1],[0]) == [-3,-2,0,1] # negatives
assert merge([3,3,3],[3,3]) == [3]*5 # duplicates
assert merge([1,1,1],[4,4,4,4]) == [1]*3 + [4]*4

assert merge_sort([6,5,4,3,2,1]) == range(1,7) # reversed-order
assert merge_sort([3,-7,1,0,-1,-5]) == [-7,-5,-1,0,1,3] # negatives
assert merge_sort([3,3,3,3]) == [3,3,3,3] # duplicates
assert merge_sort(range(50)[::-1]*2**10) # stress test
