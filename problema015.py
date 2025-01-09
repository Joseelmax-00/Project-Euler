"""*Problem*: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?"""

"""def moves(height, length):
    if height < 1 or length < 1:
        return 1
    if (height == 1 and length == 1):
        return 2
    else:
        amount = moves(height - 1 , length) + moves(height, length - 1)
        return amount
   """ 

    
    
def create_grid(sides):
    moves = 0
    grid = list()
    for column in range(0, sides):
        grid.append([1])
    for line in range(1, sides):
        grid[0].append(1)
    return grid

def fill_grid(grid):
    for line in range(1, len(grid)):
        for column in range(1, len(grid)):
            grid[column].append(grid[column-1][line] + grid[column][line-1])
    return grid

grid = create_grid(21)
grid = fill_grid(grid)
print(grid)


    
