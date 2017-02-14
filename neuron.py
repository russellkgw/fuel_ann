import random
import math

from pattern import Pattern

class Neuron(object):

    def __init__(self, patterns):
        self.patterns = patterns

        # Training varibles
        self.weight_mod_value = 0.001
        self.max_activation_output, self.iteration_error = 0.0, 0.0
        self.theta = 1.0
        self.training_iterations = 1500

    ###### Training ######

    def train_neuron(self):
        for pattern in self.patterns:
            error = 0.0

            for i in range(0, len(pattern.vector) - 1):
                print 'x'


    def fire(self, pattern):
        net = 0.0

        # Compute NET (input vector * weights)
        for i in range(0, len(pattern.vector) - 1):
            net += pattern.vector[0] * pattern.weights[0]

        # Compute bias
        theta = pattern.bias_value * pattern.bias_weight
        result = net - theta

        return sigmoid(result)

    def sigmoid(self, value):
        lambda_val = -1

        return 1 / (1 + math.e ** (lambda_val * value))