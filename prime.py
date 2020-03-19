def sieve(m,n):
    "Return all primes <= n."
    s = list(range(n+1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(sqrtn+1):
        if s[i]:
            s[i*i: n+1: i] = [0]*len(xrange(i*i, n+1, i))
    return filter(None, s)

t=input()
for _ in range(t):
    m,n=map(int, raw_input().split())
	a = sieve(m,n)
	for i in range(len(a)):
		print a[i]
        if i==len(a)-1:
            print "\n"
