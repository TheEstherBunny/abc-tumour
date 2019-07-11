
import math
import matplotlib.pyplot as pyplot
import numpy as np
def logistic(k, c_0, r, sigma, t):
	"""Simple model of the evolution of number of cancerous cells with time
	k = carrying capacity
	c_0 = initial count
	r = rate of growth
	n epsilon represents noise."""

	#t = linspace(0, 5, 100)

	n = np.random.normal(scale=sigma, size=len(t))
	c = (k / (1 + ((k / c_0) - 1) * np.exp(-r * t))) + n
	return c
if __name__ == '__main__':
	t = np.linspace(0, 5, 100)
	pyplt.title('Simple model of the evolution of number of cancerous cells with time')
	pyplt.plot(t, logistic(100, 1, 3, 1, t))
	pyplt.show()



def rms_dev(list_1, list_2):
	"""General fn for working out standard deviation between two lists that are the same size.
	Could probs use built in np.std"""
	diff = []
	for i in range(len(list_1)):
		diff.append((list_1[i] - list_2[i])**2)

	st_dev = (sum(diff)/len(list_1))**.5
	return st_dev

