### Classes definition (and class related methods):   
        
        
        
        
        
        
### Modules definition:

def iter_fibonacci(max):
    """This function is a generator for the fibonacci sequence"""
    a=1
    b=2
    while a<=max:
        yield a
        r=a+b
        a=b
        b=r
        
def prime_factors(num):
    """This function returns a list with the prime factors of num"""
    max = int(num/2)
    res = num
    div = 2
    factors = list()
    while div <= max and res != 1:
        if res%div == 0:
            res /= div
            factors.append(div)
        else:
            if div == 2:
                div += 1
            else:
                div += 2
    if factors == list():
        factors.append(num)
    return factors

def is_palindrome(num):
    """This function returns True if num is a palindrome"""
    str_num = str(num)
    for i in range(int(len(str_num) / 2)):
        if str_num[i] != str_num[-i - 1]:
            return False
    return True

def is_divisible(num, div):
    """this function returns True if the num/div is an integer (if num is divisible by div)"""
    if num % div == 0: 
        return True
    else:
        return False

def is_prime(num):
    """This function returns true if num is prime"""
    max = int(num ** 0.5+1)
    div = 2
    found = False
    while div <= max and not found:
        if num % div == 0:
            found = True
        else:
            if div==2:
                div+=1
            else:
                div+=2
    return not found

def divisors(num):
    """This function returns a list with the divisors of num"""
    max = int(num**0.5)
    res = num
    div = 1
    factors = list()
    while div <= max:
        if res%div == 0:
            factors.append(div)
            if (num/div) != div:
                factors.append(int(num/div))
        div += 1     
    return factors

def collatz(num):
    """This function prints the following number in the collatz sequence for num, if num is even it returns n/2, if not, it returns 3n+1"""
    if num == 1:
        return 0
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1

def spell_number(num):
    words = ["teen", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thir", "four", "fif", "six", "seven", "eigh", "nine", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]
    if num < 13:
        return words[num]
    if num < 20:
        return (words[num]+words[0])
    if num < 100:
        if num % 10 == 0:
            return (words[int(num/10)+18])
        else:
            return (words[int(num/10)+18]+words[num % 10])
    if num <1000:
        result = words[int(num/100)] + words[28]
        if num % 100 != 0:
            result += "and" + spell_number(num % 100)
        return result
    if num == 1000:
        return "onethousand"
        



#PRUEBA spell_number()
#print(spell_number(269))



#PRUEBA is_divisible()
#print(is_divisible(6,3))

#PRUEBA is_palindrome()
#print(is_palindrome(1001))


#PRUEBA iter_fibonacci()
#for i in iter_fibonacci(100):
#    print(i)

#PRUEBA prime_factors
#print(prime_factors(31))        

#PRUEBA divisors()
#print(divisors(1))