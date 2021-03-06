# newton's method to compute square root of value a
# increase prec (precision) for a more accurate result
def newton(a, prec):
    # Initial guess
    n = 1.0
    for _ in range(prec):
        n = (n + (a / n)) / 2
    return n

err_margin = 1e-13 # margin of error allowed
check = lambda x: x**.5 - err_margin < newton(x, 10) < x**.5 + err_margin
assert check(2) and check(10) and check(0.01)

# too big or too small values need higher prec with newton's method
check_prec = lambda x: x**.5 - err_margin < newton(x, 100) < x**.5 + err_margin
assert check_prec(500000) and check_prec(1e-5)



def karatsuba(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2
		a,b,c,d = x / 10**(nby2),x % 10**(nby2),y / 10**(nby2),y % 10**(nby2)
		ac,bd = karatsuba(a,c),karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        # writing n as 2*nby2 takes care of both even and odd length n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
		return prod

assert karatsuba(7,3) == 7*3
assert karatsuba(73,33) == 73*33
assert karatsuba(2**10,2**10) == (2**10)**2
assert karatsuba(9999,3333) == 9999*3333
assert karatsuba(9999, 22) == 9999*22
# doesn't work with odd digit and negative numbers



def euclid(a, b): # O(log(a + b))
    return a if b == 0 else euclid(b, a % b)

from fractions import gcd
check = lambda a, b: gcd(a, b) == euclid(a, b)
assert check(500, 200)
assert check(500000000,20000000)
assert check(20, 2e-5)
assert check(2e-7, 2e-5)
assert check(-20, -30)
assert check(-500, -50)



def sieve(n):
    # Return all primes <= n
    s = range(n+1)
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(sqrtn+1):
        if s[i]:
            s[i*i: n+1: i] = [0]*len(xrange(i*i, n+1, i))
    return filter(None, s)

def is_prime(n):
    # check lower boundaries on primality
    if n is 2: return True
    # 1 is not prime, even numbers > 2 are not prime
    elif n == 1 or n & 1 == 0: return False
    # check for primality using odd numbers from 3 to sqrt(n)
    sqrtn = int(round(n**0.5))
    for i in xrange(3, sqrtn+1, 2):
        if n % i == 0: return False
    # n is prime
    return True

assert filter(is_prime, range(1000)) == sieve(1000)



def factors(n): return set(reduce(list.__add__, \
    ([i, n//i] for i in range(1, int(n**.5)+1) if n%i is 0)))

assert factors(1000) == set([1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000])



def split_matrix(arr):
    h, w = arr.shape
    nrows, ncols = h/2, w/2
    return (arr.reshape(h//nrows, nrows, -1, ncols)
        .swapaxes(1,2).reshape(-1, nrows, ncols))

def combine_matrix(a,b,c,d):
    return np.vstack((np.hstack((a,b)), np.hstack((c,d))))

import numpy as np
def matrix_mult(x,y): # naive matrix multiplication
    if 1 in x.shape or 1 in y.shape:
        return x[0]*y[0]
    a,b,c,d = split_matrix(x)
    e,f,g,h = split_matrix(y)
    ae = matrix_mult(a,e)
    bg = matrix_mult(b,g)
    af = matrix_mult(a,f)
    bh = matrix_mult(b,h)
    ce = matrix_mult(c,e)
    dg = matrix_mult(d,g)
    cf = matrix_mult(c,f)
    dh = matrix_mult(d,h)
    aebg=ae+bg
    afbh=af+bh
    cedg=ce+dg
    cfdh=cf+dh
    return combine_matrix(aebg, afbh, cedg, cfdh)

def strassen(x,y):
    if 1 in x.shape or 1 in y.shape:
        return x[0]*y[0]
    a,b,c,d = split_matrix(x)
    e,f,g,h = split_matrix(y)
    P1 = strassen(a,(f-h))
    P2 = strassen((a+b),h)
    P3 = strassen((c+d),e)
    P4 = strassen(d,(g-e))
    P5 = strassen((a+d),(e+h))
    P6 = strassen((b-d),(g+h))
    P7 = strassen((a-c),(e+f))
    return combine_matrix(P5+P4-P2+P6,P1+P2,P3+P4,P1+P5-P3-P7)

import time
def benchmark(f,*args):
    s,_,t=time.time(),f(*args),time.time()
    return t-s

# n=2**7 # really slow code to check how faster than naive strassen is
# a,b=np.round(np.random.randn(n,n)*10,0),np.round(np.random.randn(n,n)*10,0)
# print 'strassen', benchmark(strassen, a, b)
# print 'naive', benchmark(matrix_mult, a, b)

def check(rows1, cols1, rows2, cols2):
    a = np.random.randint(100, size=(rows1, cols1))
    b = np.random.randint(100, size=(rows2, cols2))
    ab,ab_strassen,ab_naive = np.dot(a,b),strassen(a,b),matrix_mult(a,b)
    return np.logical_and((ab_strassen==ab).all(), (ab_naive==ab).all())

# strassen() and matrix_mult() just work for square matrices whose size is
# a power of 2. I know. Not great!
assert check(4,4,4,4) and check(32,32,32,32)



def median(arr): # O(n) median, faster than sorting and then get median
    from divideconquer import rselect
    return rselect(arr,len(arr)/2)

arr = range(1,30)
for i in range(3):
    np.random.shuffle(arr)
    assert sorted(arr)[len(arr)/2] == median(arr)+1


def get_binary(n):
    return '{0:08b}'.format(n)

assert get_binary(64) == '01000000'
assert get_binary(63) == '00111111'


def is_power_of_two(n):
    return n & (n-1) is 0

assert is_power_of_two(64)
assert not is_power_of_two(20)


def sum_of_squares(n):
    # Close form for sum(map(lambda k: k**2, range(1,n+1)))
    return 1./6.*n*(n+1)*(2*n+1)

def sum_of_cubes(n):
    # Close form for sum(map(lambda k: k**3, range(1,n+1)))
    return (1./2.*n*(n+1))**2

import random
for i in range(3):
    n = random.randint(0, 10)
    assert round(sum_of_squares(n)) == sum(map(lambda k: k**2, range(1,n+1)))
    assert round(sum_of_cubes(n)) == sum(map(lambda k: k**3, range(1,n+1)))


def pow(a, n): # O(log(n)) exponentiation
    if n is 0: return 1
    if n is 1: return a
    t = pow(a, n/2)
    return t * t * pow(a, n%2)

import math
for i in range(4):
    a = random.randint(0, 20)
    n = random.randint(0,10)
    assert pow(a, n) == math.pow(a, n)


def binomial_coefficient(n, k):
    if k > n-k:  # for smaller intermediate values
        k = n-k
    return int(reduce(lambda a,b: a*b, range((n-k+1), n+1), 1) /
                reduce(lambda a,b: a*b, range(1,k+1), 1))

    coeff = 1
    for i in range(1, k+1):
        coeff = coeff * (n-i+1) / i
    return coeff

assert binomial_coefficient(3,2) == 3
assert binomial_coefficient(9,4) ==126
assert binomial_coefficient(9,6) == 84
assert binomial_coefficient(20,14) == 38760


def norm(x, y): # Vector norm
    return (x**2 + y**2)**.5

from fractions import Fraction
def line_to_line_intersection(a,b,c,d,e,f):
    # the lines are ax+by+c=0 and dx+ey+f=0
    det = a*e - d*b
    return None if det is 0 else (Fraction((e*c - b*f),det), Fraction((a*f - d*c),det))
