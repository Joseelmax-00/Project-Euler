"""*Problem*: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

save = list()
for a in range(250,501):
    for b in range(250,500):
        c=1000-a-b
        if a**2 + b**2 == c**2:
            print("abc")
            print("{a}^2 + {b}^2 = {c}^2".format(a=a,b=b,c=c))
            save = [a,b,c]
        if a**2 + c**2 == b**2:
            print("acb")
            save = [a,b,c]
            print("{a}^2 + {c}^2 = {b}^2".format(a=a,b=b,c=c))
        if c**2 + b**2 == a**2:
            print("cba")
            save = [a,b,c]
            print("{c}^2 + {b}^2 = {a}^2".format(a=a,b=b,c=c))
        
print(save[0] * save[1] * save[2])