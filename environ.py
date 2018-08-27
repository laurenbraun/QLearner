# L.Braun 2018
# generate matrix representation of a maze environment
# output .npy file to be easily imported to a numpy array

import numpy as np
from numpy import *


# create array to be exported to a file

# 2x2 grid with walls and 2 food items
reward = np.array([[-1, 1, 0, -1],
                   [0, -1, -1, 1],
                   [0, -1, -1, 1],
                   [-1, 1, 0, -1]])


# 4x4 grid with walls
reward = np.array([[-1, 1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [1, -1, 1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, 1, -1, 1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [1, -1, -1, -1, -1, 0, -1, -1,  0, -1, -1, -1, -1, -1, -1, -1],
                   [-1, 1, -1, -1, 0, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1],
                   [-1, -1, 1, -1, -1, 0, -1, 1, -1, -1,  0, -1, -1, -1, -1, -1],
                   [-1, -1, -1, 1, -1, -1, 0, -1, -1, -1, -1,  1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, 0, -1, -1, -1, -1, 0, -1, -1,  0, -1, -1, -1],
                   [-1, -1, -1, -1, -1, 0, -1, -1, 0, -1, 0, -1, -1,  0, -1, -1],
                   [-1, -1, -1, -1, -1, -1, 0, -1, -1, 0, -1, 1, -1, -1,  0, -1],
                   [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 0, -1, -1, -1, -1, 1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, 0, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, 0, -1,  0, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1,  0, -1, 1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 0, -1]])



# save to file

# np.save('/u/braun/tlab/QLearner/data/reward_2x2.npy', reward)

np.save('/u/braun/tlab/QLearner/data/reward_4x4.npy', reward)

print("Reward matrix written.")

# write meta data to file

# meta_file = '/u/braun/tlab/QLearner/data/meta_2x2.txt'  # name text file 

meta_file = '/u/braun/tlab/QLearner/data/meta_4x4.txt'  # name text file 

with open(meta_file, 'w') as metaf:
    metaf.write('16\n')  # write x size of matrix to file
    metaf.write('16\n')  # y size


print("Meta data written.")
