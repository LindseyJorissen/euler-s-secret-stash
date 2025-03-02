def problem_25():
    amount_of_digits = 0
    fibo = [1,1]
    i = 1
    while int(amount_of_digits) < 1000:
        fibo.append(fibo[-1]+fibo[-2])
        amount_of_digits = len(str(fibo[-1]+fibo[-2]))
        i +=1
    print(f"Index : {i+2}")
    print(f"Amount of digits in result: {amount_of_digits}")

problem_25()
