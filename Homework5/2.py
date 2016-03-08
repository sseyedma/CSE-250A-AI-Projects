import numpy as np

#Parse Data
def parseData(fname):
    x = []
    f = open(fname, 'r')
    for l in f:
        x.append(l.split())
    return x

X = parseData("X.txt")
Y = parseData("Y.txt")

#compute Ti
def calculateT(X, i):
    count = 0
    for j in range(len(X)):
        if (X[j][i] == '1'):
            count += 1
    return count

#ccompute P(Y = y|X = x)
def calculatePY(p, x, determine):
    temp = 1.0
    for i in range(10):
        temp *= (1 - p[i])**int(x[i])
    if determine == 1:
        return 1 - temp
    else:
        return temp

#compute the log likelihood function
def computeL(Y, p, X):
    temp = 0.0
    for i in range(len(Y)):
        temp += np.log(calculatePY(p, X[i], int(Y[i][0])))
    return temp / len(Y)

#EM update
p = [0.5] * 10
loglikelihood = []


for k in range(64):
    loglikelihood.append(computeL(Y, p, X))
    temp_p = []
    for i in range(10):
        temp = 0.0
        for j in range(len(X)):
            if Y[j][0] == '1' and X[j][i] == '1':
                temp += p[i] / calculatePY(p, X[j], 1)
        temp_p.append(temp / calculateT(X, i))
    p = list(temp_p)



