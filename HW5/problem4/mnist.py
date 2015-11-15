import cPickle as pickle

import numpy as np

np.random.seed(1) # DO NOT MODIFY THIS LINE!

# NEURAL NETWORK CONFIGURATION
size_of_layers = [
    28 * 28, # a size of the input layer (MNIST digit data consist of 28x28 pixels)
    50, # [4.E] a size of the hidden layer
    10, # a size of the output layer
]

layers =[
    np.ones((1, size_of_layers[0])), # the input layer
    np.ones((1, size_of_layers[1])), # the hidden layer
    np.ones((1, size_of_layers[2])), # the output layer
]

weights = [
    (2 * np.random.random((size_of_layers[0], size_of_layers[1]))) - 1, # weights between the input layer and the hidden layer
    (2 * np.random.random((size_of_layers[1], size_of_layers[2]))) - 1, # weights between the hidden layer and the output layer
]

learning_rate = 0.1 # [4.E] a learning rate


def sigmoid(x):
    # a sigmoid of x

    # [4.A] FILL YOUR CODE HERE
    return 1/(1+np.exp(-x))

def propagate(x):
    # propagate an input x to the output layer

    # [4.B] FILL YOUR CODE HERE

    #Copy data to the input layer
    np.copyto(layers[0], x)

    #Compute y for the hidden layer
    layers[1]=sigmoid(
        np.dot(
            layers[0]
            ,
            weights[0]
        )
    )

    #Compute y for the output layer
    layers[2]=sigmoid(
        np.dot(
            layers[1]
            ,
            weights[1]
        )
    )

    return layers[2]

def backpropagate(y_true, learning_rate):
    # backpropagate an error from the output layer and update weights

    # [4.C] FILL YOUR CODE HERE

    #Compute deltas for output layer
    outerr = layers[2]*(1-layers[2])*(y_true-layers[2]) #(1, 10)

    #Compute deltas for hidden layers
    hiddenerr = layers[1]*(1-layers[1])*(outerr.dot(weights[1].T)) #(1, 50)

    #Change hidden-output weigths
    weights[1] = weights[1] + learning_rate*layers[1].T.dot(outerr) #(50, 10)

    #Change input-hidden weigths
    weights[0] = weights[0] + learning_rate*layers[0].T.dot(hiddenerr) #(784, 50)



# EVALUATION - DO NOT MODIFY THIS FUNCTION!
def evaluate(X, Y):
    # calculate an error of the network

    error = []
    for i in range(0, len(X)):
        x =  X[i, np.newaxis]
        y =  Y[i, np.newaxis]

        y_predicted = propagate(x)

        error.append(np.mean(np.abs(y_predicted - y)))

    return np.mean(error)

# SAMPLING CONFIGURATION
np.random.seed(1) # DO NOT MODIFY THIS LINE!

# READING DATA
with open('training.pickle', 'rb') as input_file:
    X_train, Y_train = pickle.load(input_file)
    X_train = np.array(X_train)
    Y_train = np.array(Y_train)
    print 'training data loaded'

with open('validation.pickle', 'rb') as input_file:
    X_valid, Y_valid = pickle.load(input_file)
    X_valid = np.array(X_valid)
    Y_valid = np.array(Y_valid)
    print 'validation data loaded'

# TRAINING
for iteration in xrange(50000):
    # choose a random sample of X_train and Y_train
    i = np.random.randint(0, len(X_train))
    x =  X_train[i, np.newaxis]
    y_true =  Y_train[i, np.newaxis]

    # propagate an input x
    y_predicted = propagate(x)
    # backpropagate an error and update weights
    backpropagate(y_true, learning_rate)

    if (iteration % 1000) == 0:
        print 'iteration: {0:5d} / error on validation data: {1:.15f} / y_true: {2} / y_predicted: {3}'.format(
            iteration,
            evaluate(X_valid, Y_valid),
            np.argmax(y_true),
            np.argmax(y_predicted)
        )

# EVALUATION - DO NOT MODIFY THIS SECTION!
with open('test.pickle', 'rb') as input_file:
    X_test, Y_test = pickle.load(input_file)
    X_test = np.array(X_test)
    Y_test = np.array(Y_test)

    print 'test data loaded'

print 'error on validation data: {0:.15f}'.format(evaluate(X_valid, Y_valid))
print 'error on test data: {0:.15f}'.format(evaluate(X_test, Y_test))
