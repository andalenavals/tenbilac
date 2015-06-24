﻿"""

"""

import numpy as np
import scipy.optimize

import logging
logger = logging.getLogger(__name__)

from . import act
from . import layer
from . import utils

class Tenbilac():

	"""
	This is Tenbilac
	"""
	
	def __init__(self, ni, nhs, no=1, onlyid=False):
		"""
		:param ni: Number of input features
		:param nhs: Numbers of neurons in hidden layers
		:type nhs: tuple
		:param no: Number of ouput neurons
		"""
	
		self.ni = ni
		self.nhs = nhs
		self.no = no
		self.arch = np.array([self.ni]+self.nhs+[self.no])
		
		
		self.layers = [] # We build a list containing only the hidden layers and the output layer
		for (i, nh) in enumerate(self.nhs + [self.no]):
				self.layers.append(layer.Layer(ni=self.arch[i], nn=nh, actfct=act.Sig(), name=str(i)))
		# For the output layer, set id activation function:
		self.layers[-1].actfct = act.Id()
		
		if onlyid: # Then all layers get the Id activation function:
			for l in self.layers:
				l.actfct = act.Id()
		
		logger.info("Built " + str(self))

	
	def __str__(self):
		"""
		A short description of the network
		"""
		return "Tenbilac with architecture {self.arch} and {nparams} params".format(self=self, nparams=self.nparams())

	
	def report(self):
		"""
		Returns a text about the network parameters, useful for debugging.
		"""
		txt = ["="*80, str(self)]
		for l in self.layers:
			txt.append(l.report())
		txt.append("="*80)
		return "\n".join(txt)

	
	def save(self, filepath):
		"""
		Saves self into a pkl file
		"""
		utils.writepickle(self, filepath)		
	
	
	def nparams(self):
		"""
		Returns the number of parameters of the network
		"""
		return sum([l.nparams() for l in self.layers])
		
	
	def get_params_ref(self):
		"""
		Get a single 1D numpy array containing references to all network weights and biases.
		
		We use the fact that slicing an array returns a view of it.
		"""
		
		ref = np.empty(self.nparams())
		ind = 0
		for l in self.layers:
		
			ref[ind:ind+(l.nn*l.ni)] = l.weights.flatten() # makes a copy
			ref[ind+(l.nn*l.ni):ind+l.nparams()] = l.biases.flatten() # makes a copy
			l.weights = ref[ind:ind+(l.nn*l.ni)].reshape(l.nn, l.ni) # a view
			l.biases = ref[ind+(l.nn*l.ni):ind+l.nparams()] # a view
			
			ind += l.nparams()
			
		assert ref.size == self.nparams()
		return ref


	def run(self, input):
		"""
		Propagates input through the network. This works for 1D, 2D, and 3D inputs, see layer.run().
		"""
		
		output = input
		for l in self.layers:
			output = l.run(output)
		return output
		
	
	def optcallback(self, *args):
		"""
		Function called by the optimizer to print out some info about the training progress
		"""
		#print args
		logger.info("Current training error: {0}".format(self.tmperr))
	
	
	
	def train(self, inputs, targets, errfct, maxiter=100):
		"""
		First attempt of black-box training to minimize the given errfct
		"""
			
		logger.info("Starting training with input {0} and targets {1}".format(str(inputs.shape), str(targets.shape)))
	
		params = self.get_params_ref()
		
		def f(p):
			params[:] = p
			err = errfct(self.run(inputs), targets)
			self.tmperr = err
			return err
		
		optres = scipy.optimize.fmin_bfgs(
			f, params,
			fprime=None,
			maxiter=maxiter,
			full_output=True, disp=True, retall=True, callback=self.optcallback)
	
		
		#print optres
		if len(optres) == 8:
			(xopt, fopt, gopt, Bopt, func_calls, grad_calls, warnflag, allvecs) = optres
			#finalerror = f(xopt)
			logger.info("Done with optimization, {0} func_calls and {1} grad_calls".format(func_calls, grad_calls))
			
		else:
			logger.warning("Optimization output is fishy")
	
			
	