# L.Braun 2018
# Main program to solve a gridworld maze problem

# Uses qlearner.py, environ.py

from qlearner import QLearner

a_learner = QLearner()
a_learner.load_maze('/u/braun/tlab/QLearner/data/reward_4x4.npy', '/u/braun/tlab/QLearner/data/meta_4x4.txt')

print ("testing data load\n\n")

a_learner.display_Q()
a_learner.display_R()

#print ("begin training...")

#error = a_learner.train(0.7)

#print "\n\nall error values: ", error

#a_learner.train(0.7)


#a_learner.display_Q()
#a_learner.display_R()
