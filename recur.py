def pow(b,n):
    if n==0:
        return 1
    else:
        return b*pow(b,n-1)

def hanoi(n,f,t,s):
    if n==0:
        print 'move from ' + f + ' to ' + t
    else:
        Hanoi(n-1,f,s,t)
        Hanoi(1,f,t,s)
        Hanoi(n-1,s,t,f)

def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-2, indent)+fib(n-1, indent)

def main():

if __name__=='__main__':
    main()
