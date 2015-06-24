
import numpy as np
import tenbilac

import logging
logging.basicConfig(level=logging.INFO)


(n, nrea, noise_scale, params, obs, obs_normer, params_normer, normobs, normparams, uninrea, uniparams, uniobs, ntest, testobs, normtestobs, normuniparams, normuniobs) = tenbilac.utils.readpickle("data.pkl")


net = tenbilac.net.Tenbilac(1, [10])
net.addnoise()
net.train(normobs, normparams, tenbilac.err.mse, maxiter=200)
net.save("net_mse.pkl")

