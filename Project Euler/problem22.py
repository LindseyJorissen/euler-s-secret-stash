def problem_22():
    import string

# open file and ad all data to a string
    with open("inputs/problem22.txt") as data:
        names = data.read().replace('"', '').split(",")
    names.sort()

# make dict with alphabet worth
    letters_worth = {}
    for index, alphabet_letter in enumerate(string.ascii_uppercase):
        letters_worth[alphabet_letter] = index + 1

# calculate worth of letters
    total_score = 0
    for index, name in enumerate(names):
        name_score = 0
        for char in name:
            name_score += letters_worth[char]
        total_score += (index + 1) * name_score

    print(total_score)


problem_22()
