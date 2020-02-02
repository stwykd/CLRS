def sieve(m,n):
     "Return all primes <= n."
     np1 = n + 1
     s = list(range(np1))
     s[1] = 0
     sqrtn = int(round(n**0.5))
     for i in xrange(m, sqrtn + 1):
         if s[i]:
             s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
     return filter(None, s)

t=input()
for _ in range(t):
	m,n=map(int, raw_input().split())
	a = sieve(m,n)
	for i in range(len(a)):
		print a[i]
        if i==len(a)-1:
            print "\n"
