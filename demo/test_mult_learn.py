"""
Training z = x * y

But single realziation regression, not inverse regression.

"""

import numpy as np
import tenbilac

import logging
logging.basicConfig(level=logging.INFO)


nrea = 1
ncas = 1000

# We prepare the data:

# Range of x and y
xs = np.random.uniform(-5, 5, ncas)
ys = np.random.uniform(-10, 30, ncas)

zs = xs * ys 

inputs = np.array([xs, ys])
inputs = np.tile(inputs, (nrea, 1, 1))

#inputs += 0.1*np.random.randn(inputs.size).reshape(inputs.shape)

# This is 3D (rea, features=2, case)
#print inputs
#print inputs.shape


targets = np.array([zs])

# This is 2D (feature=1, case)
#print targets
#print targets.shape



inputnormer = tenbilac.data.Normer(inputs, type="sa1")
inputs = inputnormer(inputs)
targetnormer = tenbilac.data.Normer(targets, type="sa1")
targets = targetnormer(targets)

print inputnormer
print targetnormer


dat = tenbilac.data.Traindata(inputs=inputs, targets=targets)

net = tenbilac.net.Net(ni=2, nhs=[-1], no=1, actfctname="iden", oactfctname="iden", multactfctname="iden", inames=["x", "y"], onames=["z"])
#net = tenbilac.net.Net(ni=2, nhs=[5, 5], inames=["x", "y"], onames=["z"])

net.setidentity()

# The exact solution:
#net.layers[0].weights[0,1] = 1.0
#net.layers[1].weights[0] = ((inputnormer.b[0]*inputnormer.b[1])/targetnormer.b[0])
print net.report()

#net.addnoise(multwscale=0.01, wscale=0.01, bscale=0.01)

print net.report()

training = tenbilac.train.Training(net, dat, errfctname="mse", autoplot=False, autoplotdirpath="plots")

training.bfgs(maxiter=50, gtol=1e-8)


print net.report()

outs = targetnormer.denorm(net.predict(inputs))
#outs = net.predict(inputs)

assert nrea==1

zerrs = (outs[0] - np.array([zs]))[0]
print np.mean(zerrs)
print np.std(zerrs)

import matplotlib.pyplot as plt

plt.scatter(xs, ys, c=zerrs, s=80, marker="o", edgecolors="face")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()
plt.show()


