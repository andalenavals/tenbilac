Tenbilac
========

.. image:: https://raw.githubusercontent.com/mtewes/tenbilac/master/sphinx/_static/tenbilac.png
	:align: center
	:alt: alternate text

Warning: this is undocumented work in progress! You're welcome to contact me if interested or if you have any comments, but don't expect anything useable in here for now.


About
-----

Tenbilac is a python package implementing an (experiemental) feedforward neural network designed to solve an *inverse regression* problem (aka "calibration problem" of regression, see `wikipedia <https://en.wikipedia.org/wiki/Calibration_(statistics)>`_). It performs a supervised machine learning regression from a noisy feature space to a well known explanatory space, and is trained to minimize *bias* instead of error in this explanatory space.

Despite some research, I could not find an implementation of such a "thing", so here it is. But why code this from scratch instead of using an existing neural network library ? The training is sufficiently different from what is done with normal ANNs, as tenbilac has to "experience" many realizations of a training set in order to probe bias. To simplify bookkeeping, to get more freedom in the design of the error function, and also to aim for a robust behavior (committees will have to be done anyway...), tenbilac uses black-box optimizers without back-propagation for gradient computation (for now).

Note that tenbilac is far from the "deep" learning regime! The regressions that this network should perform are relatively simple. Typical architecture would be 5 to 10 input features, 2 hidden layers of 10 nodes each, and one output. But one could well use tenbilac to calibrate the outputs of a deep learning machine or an auto-encoder, if dimensionality is a concern.

