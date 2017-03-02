import activation
import random
from pattern import Pattern
from neuron import Neuron
from vector import Vector

class Layer(object):

    def __init__(self, neuron_count, layer_type):
        self.layer_type = layer_type
        self.neurons = self.create_neurons(neuron_count)

        self.bias_value = -1
        self.bias_weight = random.random() - 0.45

        self.n = 0.01 # Learning rate
    
    def create_neurons(self, neuron_count):
        neurons = []
        for i in range(0, neuron_count):
            neurons.append(Neuron(self.layer_type))

        return neurons

    def fire_layer(self, input_vector):
        fire_results = []
        for neuron in self.neurons:
            fire_results.append(neuron.fire(input_vector))

        self.vector.values = fire_results
        return self.vector

    # def update_weights(self, target_value):
    #     for i in range(0, len(target_value)):
    #         self.vector.weights[i] += self.n * activation.sigmoid_gd(target_value[i], self.vector.values[i]) # * pattern.vector[i]


        # def update_weights(self, pattern):
    #     fire_result = self.fire(pattern)
        
    #     # Update the weights of the pattern using gradient descent on sigmoid
    #     for i in range(0, len(pattern.weights) -1):
    #         pattern.weights[i] += self.n * activation.sigmoid_gd(pattern.target_value, fire_result) * pattern.vector[i]

    #     # Update the pattern bias weight, bias value is always -1
    #     pattern.bias_weight += self.n * activation.sigmoid_gd(pattern.target_value, fire_result) * pattern.bias_value