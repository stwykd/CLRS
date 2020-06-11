def pow(b, n):
    return 1 if n is 0 else b * pow(b, n-1)


def hanoi(n, f, t, s):
    if n == 0:
        print 'move from ' + f + ' to ' + t
    else:
        hanoi(n-1, f, s, t)
        hanoi(1, f, t, s)
        hanoi(n-1, s, t, f)


from dynamicprog import memoise
@memoise
def fib(n):
    return n if n <= 1 else fib(n-2) + fib(n-1)


# a[i] and a[j] form a split inversion if a[i] > a[j] and i < j
# piggyback on the mergesort subroutine here
def count_split_inv(a,b):
    i,j,inv,c=0,0,0,[]
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
            inv+=(len(a)-i)
    return c+a[i:]+b[j:], inv


def sort_and_count_inversions(a):
    n=len(a)
    if n is 1: return a, 0
    b, x = sort_and_count_inversions(a[:n/2])
    c, y = sort_and_count_inversions(a[n/2:])
    d, z = count_split_inv(b,c)
    return d, x+y+z


from quicksort import partition
def rselect(arr, i): # find ith order statistic (ie ith smallest) in a
    if len(arr) is 1: return arr[0]
    j=partition(arr,0,len(arr))
    if j+1 == i: return arr[j]
    if j+1 > i: return rselect(arr[:j], i)
    if j+1 < i: return rselect(arr[j+1:], i-j-1)

from numpy import random
l = range(1,100)
for i in range(100): # repeat test because of randomization
    random.shuffle(l)
    n=random.randint(1,99)
    assert rselect(l,n) == n
