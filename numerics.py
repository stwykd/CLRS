def newton(prec, a):
    # Initial guess
    n = 1.0
    for _ in range(prec):
        n = (n + (a / n)) / 2
    return n


def karatsuba(a, b):
    m = int(len(str(a)) / 2)
    if m <= 1:
        # Base case, a and b cannot be split
        return a * b
    a_high, a_low = map(int, (str(a)[:m], str(a)[m:]))
    b_high, b_low = map(int, (str(b)[:m], str(b)[m:]))
    k0 = karatsuba(a_high, b_high)
    k1 = karatsuba(a_high, b_low)
    k2 = karatsuba(a_low, b_high)
    k3 = karatsuba(a_low, b_low)
    return 10**(m*2)*k0+(10**m)*(k1 + k2)+k3


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


print newton(10, 2)
print euclid(500, 200)
print karatsuba(5555, 9999)
