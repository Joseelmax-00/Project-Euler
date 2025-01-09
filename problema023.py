"""A perfect number is a number for which the sum of its proper divisors is exactly
 equal to the number. For example, the sum of the proper divisors of 28 would be
 1+2+4+7+14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it
 is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number that can be
 written as the sum of two abundant numbers is . By mathematical analysis, it can be 
 shown that all integers greater than 28123 can be written as the sum of two abundant 
 numbers. However, this upper limit cannot be reduced any further by analysis even 
 though it is known that the greatest number that cannot be expressed as the sum of 
 two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two
 abundant numbers.
"""
from itertools import product

from utils import divisors



def is_abundant(number):
    """Returns true if a number is abundant"""
    return sum(divisors(number)) - number > number

abundants = []
for number in range(1, 28123):
    if is_abundant(number):
        abundants.append(number)

can_be_written_by_sum_of_two_abundants = set()

for a,b in product(abundants, abundants):
    can_be_written_by_sum_of_two_abundants.add(a+b if a+b<28123 else 0)

print(sum(range(1,28123)) - sum(can_be_written_by_sum_of_two_abundants))