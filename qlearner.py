# L.Braun
# Objects of Qlearner class can learn the optimal route of exiting a maze
# Data could be replaced with a different object, such as
# a chemical reaction network.

# this version uses matrices already initialized to represent a maze, no actual maze object
# all foods are worth the same. goal is to eat all food

import numpy as np
from numpy import *


class QLearner():

    def __init__(self):

        # reward matrix for a 2x2 grid
        self.R = np.full((4,4), -1, dtype = int)

        # state-action matrix
        self.Q = np.zeros((4,4), dtype = int)

        self.next_states = None

        self.trained = False  # switch to true when Q matrix is trained


    def load_maze( self ):

        # TODO: make this method read in matrix data from a file

        # initialize reward matrix

        self.R = [[-1, 1, 0, -1],
                  [0, -1, -1, 1],
                  [0, -1, -1, 1],
                  [-1, 0, 0, 1]]

        # initialize next states

        self.next_states = np.array([[1, 2],
                                     [0, 3],
                                     [0, 3],
                                     [3, 3]])

    def train(self, gamma):
        """ train Q """

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
                action = np.random.choice(self.next_states[current_state])
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
