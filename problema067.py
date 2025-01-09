"""*Problem*: By starting at the top of the triangle below and
moving to adjacent numbers on the row below, the maximum
total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (vars67.txt),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem, as there
are 2^99 altogether! If you could check one trillion (1012) routes every second
it would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)"""

pyramid_1 = []
with open("vars67.txt", "r") as file:
    for line in file:
        pyramid_1.append(line.replace("\n","").split(" "))


pyramid_sum = []
pyramid_sum.append(pyramid_1[-1])
for sub_row in range(1, len(pyramid_1)):
    sum_row = []
    for entry_index in range(len(pyramid_1[-sub_row-1])):
        sum_row.append(int(pyramid_1[-sub_row-1][entry_index]) + int(max(pyramid_sum[-sub_row][entry_index], pyramid_sum[-sub_row][entry_index+1])))
    pyramid_sum.insert(0, sum_row)

print(pyramid_sum[0][0])
    
        
