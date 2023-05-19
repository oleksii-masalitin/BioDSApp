#https://www.e-olymp.com/uk/submissions/9685449
import math


def F(n):
    if n == 0:
        return 0
    elif n % 10 > 0:
        return n % 10
    else:
        return F(n // 10)


def S(p, q):
    if p == q:
        return F(p)
    dif = q - p
    step = math.floor(math.log(dif, 10))
    mod = 10 ** step
    t = q - q % mod
    return S(p, q - mod) + 5 * (mod - 1) + F(t)


while True:
    p, q = [int(i) for i in input().split()]
    if p < 0 and q < 0:
        break
    else:
        print(S(p, q))