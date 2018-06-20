# Main program to solve a gridworld maze problem

from qlearner import QLearner

a_learner = QLearner()
a_learner.load_maze()

a_learner.display_Q()
a_learner.display_R()

print ("begin training...")

#error = a_learner.train(0.7)

#print "\n\nall error values: ", error

a_learner.train(0.7)


a_learner.display_Q()
a_learner.display_R()
