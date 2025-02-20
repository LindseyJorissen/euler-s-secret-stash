from functions import sieve_of_eratosthenes
def problem10(limit):
    prime_numbers = sieve_of_eratosthenes(limit)
    sum_of_primes = sum(prime_numbers)
    print(f"The sum of all primes below two million is: {sum_of_primes}")

problem10(2000000)