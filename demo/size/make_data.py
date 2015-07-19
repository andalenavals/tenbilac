"""
Demo to make "the figure"
"""

import numpy as np
import tenbilac

import logging
logging.basicConfig(level=logging.INFO)

#np.random.seed(0)

def noise(n):
	return np.random.randn(n)
	#return 0.1*(np.exp(0.4*np.random.randn(n)) - 0.7)


# The data that will be used for training:
n = 100 # Number of "objects" (= number of parameters "theta")
nrea = 1000 # How many realizations of the data ("observations") per parameter
noise_scale = 0.1


#params = np.random.triangular(0.1, 0.2, 2.0, size=n).reshape((1, n))
params = np.linspace(0.1, 2.0, n).reshape((1, n))
obs = np.array([np.sqrt(4.0 + params**2) + noise_scale*noise(n).reshape((1, n)) for rea in range(nrea)])


# To study bias afterwards, it looks nicer to go uniform in params, and with even more nrea:
unin = 1000
uninrea = 1000
uniparams = np.linspace(0.1, 2.0, unin).reshape((1, unin))
uniobs = np.array([np.sqrt(4.0 + uniparams**2) + noise_scale*noise(unin).reshape((1, unin)) for rea in range(uninrea)])


# To plot the inverse regression, uniform in obs:
ntest = 100
testobs = np.linspace(1.6, 3, ntest).reshape((1, ntest))


# Now we norm all these. We build the Normers by using the training data (but uni would work as well...):
obs_normer = tenbilac.data.Normer(obs)
params_normer = tenbilac.data.Normer(params)

normobs = obs_normer(obs)
normparams = params_normer(params)
normtestobs = obs_normer(testobs)
normuniparams = params_normer(uniparams)
normuniobs = obs_normer(uniobs)

# And save a pkl file
pkldata = (n, nrea, noise_scale, params, obs, obs_normer, params_normer, normobs, normparams, uninrea, uniparams, uniobs, ntest, testobs, normtestobs, normuniparams, normuniobs)
tenbilac.utils.writepickle(pkldata, "data.pkl")


