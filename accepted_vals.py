import abc_tumour
import numpy as np
import matplotlib.pyplot as pyplot


"""[r, k, c_0 : must be strictly positive
we want to generate a list of accepted parameters
"""
def finding_accepted(N):
    t = np.linspace(0, 5, 100)
    results = abc_tumour.logistic(k=100, c_0=1, r=3, sigma=3, t=t)
    k_accepted = []
    c_0_accepted = []
    r_accepted = []
    sigma_accepted = []
    for i in range(N):
        k = np.random.uniform(25, 175)
        c_0 = 1
        r = np.random.uniform(0, 6)
        sigma = np.random.uniform(0,5)
        params = [k, c_0, r, sigma]
        t = np.linspace(0, 5, 100)
        estim8 = abc_tumour.logistic(params[0], params[1], params[2], params[3], t)
        d = abc_tumour.rms_dev(estim8, results)
        if d < 5:
            k_accepted.append(params[0])
            c_0_accepted.append(params[1])
            r_accepted.append(params[2])
            sigma_accepted.append(params[3])

    return k_accepted, c_0_accepted, r_accepted, sigma_accepted


num_simulations = 500000
k, c, r, s = finding_accepted(num_simulations)

print("k Acceptance rate: {}%".format(100 * len(k) / num_simulations))
print("c Acceptance rate: {}%".format(100 * len(c) / num_simulations))
print("r Acceptance rate: {}%".format(100 * len(r) / num_simulations))
print("s Acceptance rate: {}%".format(100 * len(s) / num_simulations))

xaxes = ['k','c','r','s']
yaxes = ['y1','y2','y3','y4']


# for i in range(1, 7):
#     plt.subplot(2, 3, i)
#     plt.text(0.5, 0.5, str((2, 3, i)),
#              fontsize=18, ha='center')

#for i in range(1,4):
 #   pyplot.subplot(2,2,i)
  #  pyplot.xscale('t')

pyplot.subplot(2,2,1)
pyplot.hist(k)
#plt.xscale('t')
pyplot.title('Carry capacity parameter')

pyplot.subplot(2,2,2)
pyplot.hist(c)
pyplot.title('Initial Count parameter')
#plt.xscale('t')

pyplot.subplot(2,2,3)
pyplot.hist(r)
pyplot.title('Growth rate parameter')
#plt.xscale('t')

pyplot.subplot(2,2,4)
pyplot.hist(s)
pyplot.title('Noise parameter')
#plt.xscale('t')
pyplot.show()


    #for i in range(4):
    #    plt.subplot






