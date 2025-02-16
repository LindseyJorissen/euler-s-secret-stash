def problem_6(limit):
    x = 0
    y = 0
    for i in range(limit+1):
        x += i**2
        y += i
    sqr_of_sum = y**2
    print(f"The sum of the squares is: {x}\nThe square of the sum is {sqr_of_sum}\nDifference is {sqr_of_sum - x}")

problem_6(100)