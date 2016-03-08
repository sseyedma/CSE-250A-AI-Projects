from scipy import stats
import urllib
import numpy as np
import scipy.optimize
import pylab as py
import string

def parseData(fname):
    for l in urllib.urlopen(fname):
        yield l

def sigmoid(x):
    return 1/(1+np.exp(-x))

w = [-1.53301403,-1.48429062,-2.22079829,-0.97105807,-1.86732557,-0.4883959,0.88138338,2.04514895,1.03108567,-0.04839772,1.01757989,-0.66309329,-0.14786594,0.63340024,-1.57905459,0.02907137,2.95291747,1.27848733,1.01640661,0.34069904,0.26199445,-2.27179045,-3.27406204,-3.85295161,2.42791959,0.75005343,1.79097086,-0.58383879,-1.74188449,-0.55677888,0.46715707,-0.29512893,0.18246235,0.23393425,0.27509105,-1.0230082,-0.09269407,-0.07330668,-0.78303051,-0.14496728,1.35813881,-0.98776292,0.50471822,0.7916843,0.41091148,-0.80297218,0.01772689,-1.91028338,0.60648545,-0.35100621,1.17989136,0.91618812,-0.12399735,-0.19726054,0.61538495,-1.75124618,0.39788889,0.37184725,-0.87843639,5.41213072,0.36607671,0.43560885,0.0293102,-0.66265953]
print "Reading data..."
data = list(parseData("new_test3.txt"))
print "done"
d_d = []
y_y = []
for i in range(len(data)):
    sub = string.split(data[i])
    for j in range(len(sub)):
        sub[j] = int(sub[j])
    d_d.append(sub)
    y_y.append(0.0)

print "Reading data..."
data = list(parseData("new_test5.txt"))
print "done"
for i in range(len(data)):
    sub = string.split(data[i])
    for j in range(len(sub)):
        sub[j] = int(sub[j])
    d_d.append(sub)
    y_y.append(1.0)

sum = 0.0
for i in range(400):
    if sigmoid(np.dot(w,d_d[i])) > 0.5:
        diff = 1.0 - y_y[i]
    else:
        diff = 0.0 - y_y[i]
    sum += np.abs(diff)
sum /= 400
print "error on test data 3: ", sum
sum1 = sum
sum = 0.0
for i in range(400, 800):
    if sigmoid(np.dot(w,d_d[i])) > 0.5:
        diff = 1.0 - y_y[i]
    else:
        diff = 0.0 - y_y[i]
    sum += np.abs(diff)
sum /= 400
print "error on test data 5: ", sum

print "Reading data..."
data = list(parseData("new_train3.txt"))
print "done"
d = []
y = []
for i in range(len(data)):
    sub = string.split(data[i])
    for j in range(len(sub)):
        sub[j] = int(sub[j])
    d.append(sub)
    y.append(0.0)

print "Reading data..."
data = list(parseData("new_train5.txt"))
print "done"
for i in range(len(data)):
    sub = string.split(data[i])
    for j in range(len(sub)):
        sub[j] = int(sub[j])
    d.append(sub)
    y.append(1.0)

sum = 0.0
for i in range(700):
    if sigmoid(np.dot(w,d[i])) > 0.5:
        diff = 1.0 - y[i]
    else:
        diff = 0.0 - y[i]
    sum += np.abs(diff)
sum /= 700
print "error on training data 3: ", sum
sum = 0.0
for i in range(700,1400):
    if sigmoid(np.dot(w,d[i])) > 0.5:
        diff = 1.0 - y[i]
    else:
        diff = 0.0 - y[i]
    sum += np.abs(diff)
sum /= 700
print "error on training data 5: ", sum

sum = 0.0
for i in range(1400):
    if sigmoid(np.dot(w,d[i])) >= 0.5:
        diff = 1.0 - y[i]
    else:
        diff = 0.0 - y[i]
    sum += np.abs(diff)
sum /= 1400
print "overall error: ", sum



