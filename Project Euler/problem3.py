def problem_3(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number //= 2
    for i in range(3, int(number) + 1, 2):
        while number % i == 0:
            prime_factors.append(i)
            number //= i
        if number == 1:
            break
    if number > 2:
        prime_factors.append(number)
    return max(prime_factors)

print(problem_3(600851475143))