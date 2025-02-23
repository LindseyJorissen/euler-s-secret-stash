import math

def count_divisors(n):
    divisors = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors += 2 if i * i != n else 1
    return divisors

def problem12():
    n = 1
    num = 1
    while count_divisors(num) <= 500:
        n += 1
        num += n
    print("First triangle number with over 500 divisors:", num)

problem12()
