'''


@author: fightingliu
'''
import copy, numpy as np
from conv import mini_batch_size
from numpy import random
from astropy.units import nb

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        
        
def sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z))    
def fedforward(self, a):
    for b, w in zip(self.biases, self.weights):
        a = sigmoid(np.dot(w, a) + b)
        
#         随机梯度

def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
    if test_data:n_test = len(test_data)
    n = len(training_data)
    for j in xrange(epochs):
        random.shuffle(training_data)
        mini_batches = [training_data[k:k + mini_batch_size]
        for k in xrange(0, n, mini_batch_size)]
        for mini_batch in mini_batches:
            self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch{0}：｛1｝/2{2}").format(j, self.evalutate(test_data), n_test)
            else:
                print("Epoch{0}：complete").format(j)
def update_mini_batch(self,mini_batch,eta):
    nabla_b=[np.zeros(b.shape) for b in self.biases]
    nabla_w=[np.zeros(w.shape) for w in self.weights]
    for x,y in mini_batch:
        delta_nabla_b,delta_nabla_w=self.backprop(x,y)#调用反向传播算法
        nabla_b=[nb+dnb for nb,dnb in zip(nabla_b,delta_nabla_b)]
        nabla_w=[nw+dnw for nw,dnw in zip(nabla_w,delta_nabla_w)]
        self.weights=[w-(eta/len(mini_batch))*nw
                      for w ,nw in zip(self.weights,nabla_w)]
        self.biases=[b-(eta/len(mini_batch))*nb
                     for b,nb in zip(self.biases,nabla_b)]
if __name__ == '__main__':
    net = Network([2, 3, 1])
    print(net)
