# L.Braun 2018
# generate matrix representation of a maze environment
# output .npy files to be easily imported to a numpy array

import numpy as np
from numpy import *


# create arrays to be exported to a file

reward = np.array([[-1, 1, 0, -1],
                   [0, -1, -1, 1],
                   [0, -1, -1, 1],
                   [-1, 0, 0, 1]])


next_states = np.array([[1, 2],
                        [0, 3],
                        [0, 3],
                        [3, 3]])

# save to file

np.save('/u/braun/tlab/QLearner/data/reward_4x4.npy', reward)

print("Reward matrix written.")

np.save('/u/braun/tlab/QLearner/data/next_4x4.npy', next_states)

print("Next states matrix written.")

# write meta data to file

meta_file = '/u/braun/tlab/QLearner/data/meta_4x4.txt'  # name text file 

with open(meta_file, 'w') as metaf:
    metaf.write('4\n')  # write x size of matrix to file
    metaf.write('4\n')  # y size


print("Meta data written.")
