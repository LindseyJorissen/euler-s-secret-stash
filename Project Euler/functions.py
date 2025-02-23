def sieve_of_eratosthenes(n):
    """returns a list of all prime numbers of n"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]


def triangle_numbers(limit):
    trianglenumbers = []
    current_sum = 0
    for i in range(1, limit + 1):
        current_sum += i
        trianglenumbers.append(current_sum)
    return trianglenumbers

def is_even(n):
    if n%2 == 0:
        return True

def collatz_sequence(n):
    chain = 1
    while n >1:
        if is_even(n):
            n /= 2
        else:
            n = (3*n)+1
        chain +=1
    return chain
