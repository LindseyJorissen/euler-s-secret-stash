from functions import collatz_sequence
def problem_14(limit):
    largest_chain = 0
    number_with_largest_chain = 0
    for i in range(1, limit):
        current_chain = collatz_sequence(i)
        if current_chain > largest_chain:
            largest_chain = current_chain
            number_with_largest_chain = i
    print(f"The starting number under {limit} with the largest chain is: {number_with_largest_chain} with a chain length of {largest_chain}")

problem_14(1000000)