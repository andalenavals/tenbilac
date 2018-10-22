Tenbilac
========

Tenbilac is a simple and exploratory feedforward neural network library that is designed to yield statistically _accurate_ regressions despite noisy input features. Given a special structure of the training data, the network can be trained to minimize _bias_ instead of _error_. This is useful to solve *inverse regression* problems (aka "[calibration problems](https://en.wikipedia.org/wiki/Calibration_(statistics))" of regression.

Note that the present implementation is a demonstration more than an optimized library: it is based on numpy and purely numerical differentiation with scipy.optimize.

For an introduction to the algorithm, see Section 3 and Appendix A of the related paper: https://arxiv.org/abs/1807.02120

Some technical features of tenbilac are:
- in the learning phase, it "experiences" many realizations of each training case in order to probe bias
- it offers several cost functions, including functions to predict weights for the input realizations
- it handles _masked_ numpy arrays, to accomodate for missing data
- (experimental) it offers "product units" (Durbin & Rumelhart 1989; Schmitt 2002), i.e., nodes that can take products and powers of their inputs
- it has an interface to directly train committees of networks (each member on one cpu)


Installation
------------

You could ``python setup.py install`` this, but given that this code is quite experimental,
we recommend to simply add the location of your clone of this directory to your PYTHONPATH.

To do so, if you use bash, add this line to your ``.bash_profile`` or ``.profile`` or equivalent file:

	export PYTHONPATH=${PYTHONPATH}:/path/to/tenbilac/



Directory structure
-------------------

- **tenbilac**: the python package
- **demo**: some demos and test scripts


Tutorial
--------

The documented code in ``demo/paper_figure`` serves as an example to run the basic features of tenbilac. It first generates some training data in form of noisy observations _d_ that depend on an explanatory variable theta. It then performs inverse regressions of the explanatory variable given noisy observations. By training against the _Mean Square Bias_ (MSB) cost function the results are much more accurate than with the conventional mean square error (MSE).

![Demo figure](/demo/paper_figure/paper_figure.png)
