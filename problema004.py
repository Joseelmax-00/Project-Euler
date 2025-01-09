"""*Problem*: A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

from utils import is_palindrome

mult1, mult2 = 999, 999
num = 0
found = False
while mult1 >= 100 and mult1 * mult2 > num:
    while not found:
        if is_palindrome(mult1 * mult2) and mult1 * mult2 > num:
            num = mult1 * mult2
            print("found:",num)
            found = True
        mult2-=1
        if mult2<100:
            break
            
    mult1 -= 1
    mult2 = mult1
    found = False
        

print("result:",num)

    