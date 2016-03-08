from scipy import stats
import urllib
import numpy as np
import scipy.optimize
import pylab as py

def parseData(fname):
    for l in urllib.urlopen(fname):
        yield eval(l)

print "Reading data..."
data = list(parseData("nasdaq00.txt"))
print "done"

x_t = np.array([data[i] for i in range(3,len(data))])
x_1 = np.array([data[i] for i in range(2,len(data)-1)])
x_2 = np.array([data[i] for i in range(1,len(data)-2)])
x_3 = np.array([data[i] for i in range(0,len(data)-3)])


def func(params):
    a1 = params[0]
    a2 = params[1]
    a3 = params[2]
    mean = a1*x_1 + a2*x_2 + a3*x_3
    return -np.sum(stats.norm.logpdf(x_t, loc=mean, scale=1)) / np.sqrt(2*np.pi)

initial = [1, 1, 1]
res = scipy.optimize.minimize(func, initial, method='Nelder-Mead')
print res.x

a = res.x
y = a[0]*x_1 + a[1]*x_2 + a[2]*x_3
diff = y - x_t
err = 0
for i in range(len(diff)):
    err += diff[i]**2
err = err/len(diff)
print "Error on training data: ", err

print "Reading data..."
data = list(parseData("nasdaq01.txt"))
print "done"

x_tt = np.array([data[i] for i in range(3,len(data))])
x_1t = np.array([data[i] for i in range(2,len(data)-1)])
x_2t = np.array([data[i] for i in range(1,len(data)-2)])
x_3t = np.array([data[i] for i in range(0,len(data)-3)])
y = a[0]*x_1t + a[1]*x_2t + a[2]*x_3t
diff = y - x_tt
err = 0
for i in range(len(diff)):
    err += diff[i]**2
err = err/len(diff)
print "Error on testing data: ", err



