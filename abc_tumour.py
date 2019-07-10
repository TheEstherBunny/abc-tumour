
import math
import matplotlib.pylab as pylb
import numpy as np
def logistic(k, c_0, r, e, t):
	"""Simple model of the evolution of number of cancerous cells with time
	#e. epsilon represents noise."""	#
	c = (k/(1+(k/(c_0-1))*np.exp(-r*t)) + e

t = linspace(0, 100, 100)
s = np.random.normal(mu, sigma, 1000)


pylb.plot(logistic(1, 100, 45,45, t))
	pylb.plot(show)