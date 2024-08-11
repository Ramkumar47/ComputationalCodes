# Dense Neural Network development code
Here the fortran code for the generalized fully connected dense network
was developed for custom use

As the validation, the absorbance spectrum approximation with noise
removal was performed with this code.

Here, the Adam optimizer algorithm was implemented in the code


The network doesn't train to the expected value as the derivative of loss
function goes to zero because of symmetry patterns present in the dataset.

This problem can be fixed if using stochastic gradient descent, which will be
the next step to implement.
