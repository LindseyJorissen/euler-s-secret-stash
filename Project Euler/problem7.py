def problem_7(limit):
    lijst = []
    num = 2
    while len(lijst) < limit:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            lijst.append(num)
        num += 1
    print(f"The {limit}th prime number is: {lijst[-1]}")
problem_7(10001)
