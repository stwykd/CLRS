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



def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)

from fractions import gcd
check = lambda a, b: gcd(a, b) == euclid(a, b)
assert check(500, 200)and check(500000000,20000000)and check(20, 2e-5)\
and check(2e-7, 2e-5)and check(-20, -30)and check(-500, -50)




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
