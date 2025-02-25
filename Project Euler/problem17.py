import inflect
def problem_17():
    p = inflect.engine()
    total_letters = 0
    for i in range(1,1001):
        text_version_of_num = p.number_to_words(i)
        total_letters += len(text_version_of_num.replace(" ", "").replace("-", ""))
    print(f"The total amount of letters used to spel the numbers is {total_letters}")
problem_17()