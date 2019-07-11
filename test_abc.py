import abc_tumour
import matplotlib.pyplot as pyplot
import numpy as np
def test_logistic():
    print('Hi, testing function')

    assert abc_tumour.logistic(100, 1, 3, 0, np.array([0]) == np.array([1]))
    assert np.abs(abc_tumour.logistic(150, 1, 4, 0, np.array([10000]))- np.array([150])) < 10**-6




def test_stdev():

    assert abc_tumour.rms_dev([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 0
    assert abc_tumour.rms_dev([2, 3, 4, 5, 6], [3, 4, 5, 6, 7]) == 1