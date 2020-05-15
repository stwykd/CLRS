# counting sort is O(n) sorting algorithm not based on comparisons
# useful with many duplicates, and a narrow range of possible values
def counting_sort(a):
    # counts[i] is how many times i appears in a
    # eg a is [2,2,2,3], then counts[2] is 3
    counts, sorted_ = [0]*(max(a)+1), []
    for k in a:
        counts[k] += 1
    for i in range(len(counts)):
        sorted_.extend([i]*counts[i])
    return sorted_

a = [1, 4, 3, 2, 4, 3, 8, 3]
assert sorted(a) == counting_sort(a)
