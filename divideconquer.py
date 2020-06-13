from operator import itemgetter, attrgetter

def naive_closest_pair(point):
    n = len(point)
    return float('inf'), (None, None) if n < 2 else min(
        ((abs(point[i] - point[j]), (point[i], point[j]))
        for i in range(n-1) for j in range(i+1,n)), key=itemgetter(0))

def closest_pair(points):
    px, py = sorted(points,key=attrgetter('real')),sorted(points,key=attrgetter('imag'))
    return _closest_pair(px, py)

def _closest_pair(px, py):
    n = len(px)
    if n <= 3:
        return naive_closest_pair(px)
    pl, pr, yl, yr = px[:n/2], px[n/2:], [], []
    x_divider = pl[-1].real
    [yl.append(p) if p.real <= x_divider else yr.append(p) for p in py]
    dl, pairl = _closest_pair(pl, yl)
    dr, pairr = _closest_pair(pr, yr)
    dm, pairm = (dl, pairl) if dl < dr else (dr, pairr)
    close_y = [p for p in py  if abs(p.real-x_divider) < dm]
    n_close_y = len(close_y)
    if n_close_y > 1:
        closest_y = min( ((abs(close_y[i] - close_y[j]), (close_y[i], close_y[j]))
                         for i in range(n_close_y-1)
                         for j in range(i+1,min(i+8, n_close_y))),
                        key=itemgetter(0))
        return (dm, pairm) if dm <= closest_y[0] else closest_y
    else:
        return dm, pairm

import time
def benchmark(f,*args):
    s,_,t=time.time(),f(*args),time.time()
    return t-s

points = [(5+9j),(9+3j),(2+0j),(8+4j),(7+4j),(9+10j),(1+9j),(8+2j),10j,(9+6j)]
print  closest_pair(points), naive_closest_pair(points)
print 'naive', benchmark(naive_closest_pair,points*300)
print 'divide and conquer', benchmark(closest_pair,points*300)



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
