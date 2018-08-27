# L.Braun
# maze class to be learned by a learning agent
# 7/3: NOT USING THIS CLASS


import numpy as np
from numpy import *


class Maze():

    # TODO: need to make data members to represent "edge list" ie next possible state
    # each index of the grid needs an integer to track the number: could just add the indices


    def __init__( self ):
        """ initialize maze gridworld """

        self.grid = [[0,0,0],[0,0,0],[0,0,0]]

        # 0 - empty
        # 1 - food
        # 2 - exit

        self.grid[0][1] = 1  # food
        self.grid[1][2] = 1  # food
        self.grid[1][2] = 1  # food
        self.grid[0][2] = 1  # food

        self.grid[2][2] = 2  # exit maze


    def display( self ):
        """ display maze in array format """
    
        for row in self.grid:
            print row



    def get_next_states( self, current_state = [] ):
        """ return a list of possible next states """
    
        x = current_state[0]
        y = current_state[1]
        next_states = [ [ (x+1)%len(self.grid[0]) , y ], [ x , (y+1)%len(self.grid) ], [ (x-1)%len(self.grid[0]) , y ], [ x , (y-1)%len(self.grid) ] ]
        
        return next_states


    def get_num_states( self ):
        """ return total number of states """

        return len(self.grid) * len(self.grid[0])

    def get_random_state( self ):
        """ return coordinates of a random state in the maze """

        x = np.random.randint(0, len(self.grid[0]))
        y = np.random.randint(0, len(self.grid))
        
        random_state = [x,y]  # select random initial state

        return random_state


    def is_exit( self, current_state=[] ):
        """ return true if arg coordinate is the exit """

        x = current_state[0]
        y = current_state[1]

        if self.grid[x][y] == 2:  # 2 means exit
            result = True

        else:
            result = False 

        return result










