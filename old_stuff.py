alphabet = [[1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]]
    alphabet.insert(1, [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1])
    alphabet.insert(2, [1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1])
    alphabet.insert(3, [1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0])
    alphabet.insert(4, [1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1])
    alphabet.insert(5, [1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0])
    alphabet.insert(6, [1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1])
    alphabet.insert(7, [1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1])
    alphabet.insert(8, [1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1])
    alphabet.insert(9, [1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0])
    alphabet.insert(10, [1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1])
    alphabet.insert(11, [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1])
    alphabet.insert(12, [1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1])
    alphabet.insert(13, [1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1])
    alphabet.insert(14, [1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1])
    alphabet.insert(15, [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0])
    alphabet.insert(16, [1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1])
    alphabet.insert(17, [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1])
    alphabet.insert(18, [1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1])
    alphabet.insert(19, [1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0])
    alphabet.insert(20, [1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1])
    alphabet.insert(21, [1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0])
    alphabet.insert(22, [1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1])
    alphabet.insert(23, [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1])
    alphabet.insert(24, [1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0])
    alphabet.insert(25, [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1])

myNeuron = Neuron(alphabet_array())
myNeuron.train_neuron(0)
myNeuron.eval_neuron(0)

# from activation import Activation -- module
import random

class Neuron(object):

    def __init__(self, vectors):
        self.vectors = vectors
        self.weights = self.generate_random_weights(len(self.vectors))

        # Training varibles
        self.weight_mod_value = 0.001
        self.max_activation_output, self.iteration_error = 0.0, 0.0
        self.theta = 1.0
        self.training_iterations = 1500

    ###### Weights ######

    def generate_zero_updates(self, number):
        weight_updates = []
        for i in range(0, number - 1):
            weight_updates.insert(i, 0.0)

        return weight_updates

    def generate_random_weights(self, number):
        weights = []
        for i in range(0, number - 1):
            weights.insert(i, random.random() - 0.5)

        return weights

    ###### Learning method ######

    def gradient_descent(self, minuend, activation):
        return (minuend - activation) ** 2

    ###### Training ######

    def train_neuron(self, expected_index):
        for iteration in range(1, self.training_iterations):
            self.max_activation_output, self.iteration_error = 0.0, 0.0
            weight_update_values = self.generate_zero_updates(len(self.vectors))

            # Each vector in vectors array
            for j in range(0, len(self.vectors) - 1):
                vector = self.vectors[j]
                activation_output = self.theta * self.weights[0]

                # Each element of vector multiply by weight
                for k in range(0, len(vector) - 1):
                    activation_output += vector[k] * self.weights[k + 1]

                # If the vector we are looking for
                if j == expected_index:
                    self.iteration_error += self.gradient_descent(1.0, activation_output)
                    weight_update_values[0] += (1.0 - activation_output) * self.theta

                    for a in range(0, len(vector) - 1):
                        weight_update_values[a + 1] += (1.0 - activation_output) * vector[a]
                else:
                    self.iteration_error += self.gradient_descent(0.0, activation_output)
                    weight_update_values[0] += (0.0 - activation_output) * self.theta

                    for a in range(0, len(vector) - 1):
                        weight_update_values[a + 1] += (0.0 - activation_output) * vector[a]

                if activation_output > self.max_activation_output:
                    self.max_activation_output = activation_output

            # Update the weights for next iteration
            for b in range(0, len(self.weights) - 1):
                self.weights[b] += self.weight_mod_value * weight_update_values[b]

    ###### Evaluate the trained neuron ######

    def eval_neuron(self, eval_index):
        eval_vector = self.vectors[eval_index]
        activation_output = self.weights[0] * self.theta

        for e in range(0, len(eval_vector) - 1):
            activation_output += eval_vector[e] * self.weights[e + 1]

        eval_error = self.gradient_descent(self.max_activation_output, activation_output)
        print 'Eval error: ' + str(eval_error)

        if eval_error < 0.000001:
            print 'MATCH!'
        else:
            print '!!! NO_MATCH! !!!'