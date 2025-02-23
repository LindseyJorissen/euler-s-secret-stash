def problem12():
    sum_list = []
    with open("inputs/problem13.txt", "r") as file:
        for row in file:
            sum_list.append(int(row.strip()))
    sum_all_numbers = sum(sum_list)
    print(f"List of numbers:{sum_list}")
    print(f"Sum of all numbers: {sum_all_numbers}")
    sum_all_numbers_string = str(sum_all_numbers)
    print(f"First 10 digits of this number: {sum_all_numbers_string[0:10]}")
problem12()