"""*Problem*: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

from utilidades import is_prime
sum=2
for i in range(3,2_000_000, 2):
    if is_prime(i):
        sum += i
print(i)
print(sum)