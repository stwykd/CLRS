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

def fib(n, indent):
    if n<=1:
        indent = ' '*(len(indent)-4)
        return 1
    else:
        indent+='   '
        return fib(n-2, indent)+fib(n-1, indent)


def main():
    print fib(5, '    ')

if __name__=='__main__':
    main()
