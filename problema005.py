"""*Problem*: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

from utils import is_divisible

found = False
num = 0
while not found:
    num += 1
    divs=list()
    #if num % 10000 == 0:
    #    print("testing:", num)
    for i in range(2,21):
        if is_divisible(2520*num, i):
            divs.append(i)
        else:
            break
    if divs[-1]>17:
        print(2520*num, divs)
    if divs[-1] == 20:
        found = True
    
print("result:",2520*num)

"""Viejo código, el anterior está cambiado para solo comprobar los múltiplos de 2520, este chequea todos los números:

found = False
num = 0
while not found:
    num += 1
    divs=list()
    #if num % 10000 == 0:
    #    print("testing:", num)
    for i in range(2,21):
        if is_divisible(num, i):
            divs.append(i)
        else:
            break
    if divs[-1]>17:
        print(num, divs)
    if divs[-1] == 20:
        found = True
    
print("result:",num)
"""
