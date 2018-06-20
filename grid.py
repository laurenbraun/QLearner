# L.Braun
# grid world to be navigated by a learner

#import numpy as np
#grid = np.zeros(shape=(4,4))

# TODO: abstract this into a class
#class Grid():

    #def __init__(self):

grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# 0 - empty
# 1 - wall
# 2 - cell that has been visited
# 3 - exit!

grid[0][3] = 1  # wall
grid[1][3] = 1  # wall
grid[1][0] = 1  # wall
grid[1][2] = 1  # wall
grid[2][3] = 1  # wall
grid[0][2] = 1  # wall
grid[0][3] = 1  # wall

grid[3][3] = 3  # exit maze

def display( grid ):
    """ display maze in array format """
    
    for row in grid:
        print row

def modify( grid, x, y, z ):
    """ modify cell in maze at location (x,y) to new value z """
    
    grid[x].pop(y)
    grid[x].insert(y, z)


def search(grid, x, y):
    """ arg is the coordinate of a point in the maze.
        return true if at the exit, false if at a wall or
        at a visited cell. """

    if grid[x][y] == 3:
        print 'exited maze. good job.'
        return True

    if grid[x][y] == 1:
        print x,',',y,' is a wall'
        modify(grid, x, y, 2)  # mark as visited
        return False

    if grid[x][y] == 2:
        print 'already visited %d,%d' % (x,y)
        return False
    
    if ((x < len(grid) - 1) and search(x+1, y)) or (y>0 and search(x, y-1)) or (x>0 and search(x-1, y)) or (y<len(grid-1 and search(x, y+1))):
        return true

    return false

# display maze
display(grid)
print ''




if search(grid,0,3) == False:
    print 'returned false.\n'

print 'updated maze:\n'
display(grid)
print '' 

if search(grid,0,3) == False:
    print 'returned false.\n'

if search(grid,3,3) == False:
    print 'returned false.'
else:
    print 'returned true.'





