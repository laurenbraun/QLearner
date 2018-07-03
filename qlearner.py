# L.Braun 2018
# Objects of Qlearner class can learn the optimal route of exiting a maze
# Data could be replaced with a different object, such as
# a chemical reaction network.

# this version uses matrices already initialized to represent a maze, no actual maze object
# all foods are worth the same. goal is to eat all food

import numpy as np
from numpy import *


class QLearner():

    def __init__( self ):

        # reward matrix for a 2x2 grid
        #self.R = np.full((4,4), -1, dtype = int)
        self.R = None

        # state-action matrix
        #self.Q = np.zeros((4,4), dtype = int)
        self.Q = None

        self.trained = False  # switch to true when Q matrix is trained


    def load_maze( self, R_data, meta_data ):
        """ load matrix data into class data members. R_data, next_data are .npy array files.
            meta_data is a txt file that gives shape of matrices to initialize Q """

        # initialize matrices from shape given in file
        with open(meta_data, 'r') as mfile:
            
            array_shape = mfile.readlines()  # list of each line, each line is one int
            x = int(array_shape[0])
            y = int(array_shape[1])

            # initialize Q matrix of shape (x,y)
            self.Q = np.zeros((x,y), dtype = int)

        # load data into reward matrix
        self.R = np.load(R_data)


    
    def get_possible_actions( self, state ):
        """ return array of possible actions to take from state given in arg """

        all_actions = self.R[state]  # get row from R matrix for this state
        valid_actions = np.where(all_actions >= 0)  # save only valid moves
        return valid_actions


    def train( self, gamma ):
        """ train Q. gamma is an int between 0 and 1 """

        i = 0  # tracker
        # total_reward = 0  # track total reward over all interations
        food_eaten = 0
        eaten_states = []
        num_steps = 0
        error = []

        # while self.trained == False
        while i < 10:

            # select random initial state
            current_state = np.random.randint(0,4)

            # do while all 2 foods have not been eaten..once eaten both, at the 'exit state' 
            while food_eaten < 2:
                
               # print "current state: ", current_state

                # select an action
                pos_acts = self.get_possible_actions(current_state)
                action = np.random.choice(pos_acts[0])
               
               # print "action: ", action

                # add reward for this action
                # total_reward += self.R[current_state][action]

                # get all possible next Q values
                next_q = []
                for next_possible in self.next_states[action]:
                    next_q.append(self.Q[action][next_possible])

                # get max Q value
                max_reward = max(next_q)
               # print "max reward of next action: ", max_reward

                self.Q[current_state][action] = self.R[current_state][action] + gamma * max_reward

                if self.R[current_state][action] == 1:
                    
                    # check if this state has already been eaten
                    if (current_state, action) not in eaten_states: 
                        food_eaten = food_eaten + 1  # increase total eaten
                        eaten_states.append((current_state, action))  # add state action pair to eaten list


                # update current state to chosen action
                current_state = action

                # increment number of steps this time through grid
                num_steps = num_steps + 1

            error.append(num_steps - 2)
            i = i + 1  # update tracker

        #return error
        print (error)

    def display_Q( self ):
        print (self.Q)
        print ("")

    def display_R( self ):

        for row in self.R:
            print (row)

        print ("")
