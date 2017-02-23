import random
import math
import activation

from pattern import Pattern

class Neuron(object):

    def __init__(self):
        self.weight = random.random() - 0.45

    ###### Training ######

    def fire(self, pattern):
        # Compute NET (input vector * weights)
        net = 0.0
        for i in range(0, len(pattern.vector) - 1):
            net += pattern.vector[i] * pattern.weights[i]

        # Compute bias
        theta = pattern.bias_value * pattern.bias_weight

        result = net - theta
        return activation.sigmoid(result)

    # def update_weights(self, pattern):
    #     fire_result = self.fire(pattern)
        
    #     # Update the weights of the pattern using gradient descent on sigmoid
    #     for i in range(0, len(pattern.weights) -1):
    #         pattern.weights[i] += self.n * activation.sigmoid_gd(pattern.target_value, fire_result) * pattern.vector[i]

    #     # Update the pattern bias weight, bias value is always -1
    #     pattern.bias_weight += self.n * activation.sigmoid_gd(pattern.target_value, fire_result) * pattern.bias_value

    # def print_fire_results(self):
    #     for pattern in self.patterns:
    #         print 'Letter: ' + pattern.letter + ' expected: ' + str(pattern.target_value) + ' fire result: ' + str(round(self.fire(pattern), 1))

    # def eval_neuron(self, index):
    #     if round(self.fire(self.patterns[index]), 1) > 0.9:
    #         print 'MATCH'
    #     else:
    #         print 'NO_MATCH!'
