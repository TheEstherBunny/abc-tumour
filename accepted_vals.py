import abc_tumour
import numpy as np
import matplotlib.pyplot as pyplot


"""[r, k, c_0 : must be strictly positive
we want to generate a list of accepted parameters
"""
def finding_accepted(N):
    t = np.linspace(0, 5, 100)
    results = abc_tumour.logistic(100, 1, 3, 1, t)
    k_accepted = []
    c_0_accepted = []
    r_accepted = []
    sigma_accepted = []
        for i in range(N):
            k = np.random.uniform(100, 200)
            c_0 = np.random.uniform(0,100)
            r = np.random.uniform(0, 2)
            sigma = np.random.uniform(0,2)
            params = [k, c_0, r, sigma]
            t = np.linspace(0, 5, 100)
            estim8 = abc_tumour.logistic(params[0], params[1], params[2], params[3], t)
                if abc_tumour.rms_dev(estim8) - abc_tumour.rms_dev(results)< 5:
                    k_accepted.append(params[0])
                    c_0_accepted.append(params[1])
                    r_accepted.append(params[2])
                    sigma_accepted.append(params[3])
                    return
        return  k_accepted
        return  c_0_accepted
        return r_accepted
        
    finding_accepted(10000)






