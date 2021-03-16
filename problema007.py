"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
from utilidades import is_prime

found = False
i=3
primes=1
while not found:
    if is_prime(i):
        primes += 1
        if primes % 100 == 0:
            print("prime number", primes, "is", i)
    if primes == 10001:
        print(i)
        found = True
    i += 2
        
    