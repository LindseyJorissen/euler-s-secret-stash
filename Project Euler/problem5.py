def problem_5():
    num = 20
    while True:
        if all(num % i == 0 for i in range(2, 21)):
            print(num)
            break
        num += 20
problem_5()