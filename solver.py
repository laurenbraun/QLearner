# L.Braun 2018
# Main program to solve a gridworld maze problem

# Uses qlearner.py, environ.py

from qlearner import QLearner
import pylab as plt

my_learner = QLearner()
my_learner.load_maze('/u/braun/tlab/QLearner/data/reward_4x4.npy', '/u/braun/tlab/QLearner/data/meta_4x4.txt')

#print ("testing data load\n\n")

#my_learner.display_Q()
#my_learner.display_R()

print ("begin training...")

reward = my_learner.train(0.7)

my_learner.display_Q()
my_learner.display_R()

steps = my_learner.test()
print "steps"
print steps
print ""

#plt.plot(reward)
#plt.show()


