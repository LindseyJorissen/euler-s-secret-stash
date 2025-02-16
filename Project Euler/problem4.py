def problem_4():
    max_palindrome = 0
    for j in range(999, 100, -1):
        for i in range(j, 100, -1):
            totaal = i * j
            if totaal <= max_palindrome:
                break
            if str(totaal) == str(totaal)[::-1]:
                max_palindrome = totaal
    print(max_palindrome)
problem_4()
