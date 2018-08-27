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

steps = my_learner.test(7)  # 7 foods in 4x4 maze
print ("steps")
print (steps)
print ("")

plt.hist(reward, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Episodes required to reach 200')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()



