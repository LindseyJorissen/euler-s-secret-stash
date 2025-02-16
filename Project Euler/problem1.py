def problem_1(number):
    som = 0
    for i in range(0,number):
        if i % 3 == 0 or i % 5 == 0:
            som += i
    return som

print(problem_1(1000))
