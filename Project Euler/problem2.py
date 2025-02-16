def problem_2(limit):
    fibo_list = [0, 1]
    total = 0
    while fibo_list[-1] + fibo_list[-2] < limit:
        fibo_list.append(fibo_list[-2] + fibo_list[-1])
    for i in fibo_list:
        if i % 2 == 0:
            total += i
    print(total)

problem_2(4000000)