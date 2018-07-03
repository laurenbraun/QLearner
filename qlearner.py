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

        # reward matrix 
        self.R = None

        # state-action matrix
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


        # load numpy array datafile into reward matrix
        self.R = np.load(R_data)


    
    def get_possible_actions( self, state ):
        """ return list of possible actions to take from state given in arg """

        # get row from R matrix for this state
        all_actions = self.R[state]
        valid_actions = np.where(all_actions >= 0)  # save only valid moves
        
        return valid_actions[0]



    def train( self, gamma ):
        """ train Q. gamma is an int between 0 and 1 """

        i = 0  # tracker
        total_rewards = []  # track reward total over all iterations
        food_eaten = 0
        eaten_states = []

        # while self.trained == False
        while i < 500:

            # select random initial state
            current_state = np.random.randint(0,4)

            # do while all 2 foods have not been eaten..once eaten both, at the 'exit state' 
            while food_eaten < 2:
                
                # select an action
                pos_acts = self.get_possible_actions(current_state)
                action = int(np.random.choice(pos_acts))
            
                # consider this action as current state and get next possible actions
                next_pos_acts = self.get_possible_actions(action)

                # get all possible next Q values
                next_q = []
                for maybe in next_pos_acts:
                    next_q.append(self.Q[action][maybe])

                # get max Q value
                max_reward = max(next_q)

                # update Q matrix
                self.Q[current_state][action] = self.R[current_state][action] + gamma * max_reward

                # check to make sure we don't divide by 0
                if (np.max(self.Q) > 0):
                    curr_reward = np.sum(self.Q/np.max(self.Q) * 100)  # get current rewards from Q
                    total_rewards.append(curr_reward)  # add this round's reward to total reward list

                
                # check if we are at a food item
                if self.R[current_state][action] == 1:
                
                    # check if this state has already been eaten
                    if (current_state, action) not in eaten_states: 
                        food_eaten = food_eaten + 1  # increase total eaten
                        eaten_states.append((current_state, action))  # add state action pair to eaten list


                # update current state to chosen action
                current_state = action
                
            i = i + 1  # update tracker



        return total_rewards




    def display_Q( self ):
        print (self.Q)
        print ("")

    def display_R( self ):

        for row in self.R:
            print (row)

        print ("")
