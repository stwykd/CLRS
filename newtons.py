def newton(prec, a):
    n = 1.0
    for _ in range(prec):
        n = (n + (a / n)) / 2
    return n

print newton(10, 2)