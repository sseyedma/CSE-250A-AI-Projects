import numpy as np
import sys
import matplotlib.pyplot as plt

def parseData(fname):
	x = []
	for l in open(fname):
		l = l.split()
		for i in range(len(l)):
			x.append(float(l[i]))
	return np.array(x)
### read in all data
observation = parseData("observations.txt")
pi = np.array([float(l) for l in open("initialStateDistribution.txt")])
emission = parseData("emissionMatrix.txt").reshape(26, 2)
transition = parseData("transitionMatrix.txt").reshape(26, 26)

### initilize trellis matrix
trellis = np.zeros((26, len(observation)), dtype=float)
### compute trellis matrix
trellis[:, 0] = np.log(pi) * np.log(emission[:, observation[0]])
for t in range(1, len(observation)):
	for j in range(26):
		trellis[j][t] = max(trellis[:, t - 1] + np.log(transition[:, j])) + np.log(emission[j][observation[t]])

### backtracking for states
s = np.array([0.0 for i in range(len(observation))])
s[-1] = np.argmax([trellis[i][-1] for i in range(26)])
for t in range(1, len(observation)):
	s[-1 - t] = np.argmax(trellis[:, -1 - t] + np.log(transition[:, s[-t]]))
s += 1

### plot the graph
plt.plot(s)
plt.ylabel('state')
plt.xlabel('time')
plt.show()





