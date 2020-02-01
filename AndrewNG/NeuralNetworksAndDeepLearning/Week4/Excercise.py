import numpy as np
import h5py
import matplotlib.pyplot as plt
np.random.seed(1)

def display_shape_initialize_parameters_deep(parameters):
    print(parameters['W1'].shape)
    print(parameters['b1'].shape)
    print(parameters['W2'].shape)
    print(parameters['b2'].shape)
    return None


def sigmoid(Z):
    A = 1 / (1 + np.exp(-Z))
    activation_cache = Z
    return A, activation_cache


def relu(Z):
    A = np.maximum(0, Z)
    activation_cache = Z
    return A, activation_cache


def relu_backward(dA, cache):
    Z = cache
    dZ = np.array(dA, copy=True)  # just converting dz to a correct object.
    # When z <= 0, you should set dz to 0 as well.
    dZ[Z <= 0] = 0
    return dZ


def sigmoid_backward(dA, cache):
    Z = cache
    s = 1 / (1 + np.exp(-Z))
    dZ = dA * s * (1 - s)
    return dZ


def initialize_parameters_deep(layer_dims):
    parameters = dict()
    for layer_no in range(1, len(layer_dims)):
        if layer_no > 0:
            parameters['W' + str(layer_no)] = np.random.randn(layer_dims[layer_no], layer_dims[layer_no - 1]) * 0.01
            parameters['b' + str(layer_no)] = np.zeros((layer_dims[layer_no], 1))
    return parameters


def linear_forward(A, W, b):
    Z = np.dot(W, A) + b
    cache = (A, W, b)
    return Z, cache


def linear_activation_forward(A_prev, W, b, activation):
    Z, linear_cache = linear_forward(A_prev, W, b)
    if activation == "sigmoid":
        A, activation_cache = sigmoid(Z)
    elif activation == "relu":
        A, activation_cache = relu(Z)
    cache = (linear_cache, activation_cache)
    return A, cache


def L_model_forward(X, parameters, layer_dims):
    caches = []
    A = X
    L = len(layer_dims)   # L is number of layers
    for l in range(1, L):
        A_prev = A
        A, cache = linear_activation_forward(A_prev,
                                             parameters['W' + str(l)],
                                             parameters['b' + str(l)],
                                             activation='relu')
        caches.append(cache)
    AL, cache = linear_activation_forward(A,
                                          parameters['W' + str(L)],
                                          parameters['b' + str(L)],
                                          activation='sigmoid')
    caches.append(cache)


def compute_cost(AL, Y):
    m = Y.shape[1]
    cost = -1 / m * (np.dot(np.log(AL), Y.T) + np.dot(np.log(1 - AL), (1 - Y).T))
    cost = np.squeeze(cost)
    return cost


def linear_backward(dZ, cache):
    A_prev, W, b = cache
    m = A_prev.shape[1]
    dW = 1/m * np.dot(dZ, A_prev.T)
    db = 1/m * np.sum(dZ, axis=1, keepdims=True)
    dA_prev = np.dot(W.T, dZ)
    return dA_prev, dW, db


def linear_activation_backward(dA, cache, activation):
    linear_cache, activation_cache = cache
    if activation == "relu":
        dZ = relu_backward(dA, activation_cache)
    elif activation == "sigmoid":
        dZ = sigmoid_backward(dA, activation_cache)
    dA_prev, dW, db = linear_backward(dZ, linear_cache)
    return dA_prev, dW, db


def L_model_backward(AL, Y, caches):
    grads = {}
    L = len(caches)  # the number of layers
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)  # after this line, Y is the same shape as AL
    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
    current_cache = caches[-1]
    grads["dA" + str(L - 1)], grads["dW" + str(L)], grads["db" + str(L)] = \
        linear_backward(sigmoid_backward(dAL, current_cache[1]), current_cache[0])
    for l in reversed(range(L - 1)):
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_backward(sigmoid_backward(dAL, current_cache[1]), current_cache[0])
        grads["dA" + str(l)] = dA_prev_temp
        grads["dW" + str(l + 1)] = dW_temp
        grads["db" + str(l + 1)] = db_temp
    return grads


def update_parameters(parameters, grads, learning_rate):
    L = len(parameters) // 2  # number of layers in the neural network
    for l in range(L):
        parameters["W" + str(l+1)] = parameters["W" + str(l + 1)] - learning_rate * grads["dW" + str(l + 1)]
        parameters["b" + str(l+1)] = parameters["b" + str(l + 1)] - learning_rate * grads["db" + str(l + 1)]
    return parameters

layer_dims = [5, 4, 3]  # 5 features n_x, 4 nodes in hidden layer , 3 nodes in outputs
parameters = initialize_parameters_deep(layer_dims)
display_shape_initialize_parameters_deep(parameters)






