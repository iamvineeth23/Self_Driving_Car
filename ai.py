# AI for Self Driving Car

# Importing the libraries

import numpy as np
import random 
import os # To loading and saving
import torch
import torch.nn #will get q-values
import torch.nn.functional as F #functions for NN eg. loss functions
import torch.optim as optim #for optimiser to perform stochastic gradient descent
import torch.autograd as autograd #Variable class to convert tensors into array
from torch.autograd import Variable