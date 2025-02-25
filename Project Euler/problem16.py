def problem_16():
    power_result = 2**1000
    sum_of_nums = 0

    for digit in str(power_result):
        sum_of_nums += int(digit)

    print(sum_of_nums)

problem_16()
