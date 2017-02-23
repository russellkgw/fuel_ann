import random
from pattern import Pattern
from neuron import Neuron

class Layer(object):

    def __init__(self, neuron_count, layer_type):
        self.neurons = self.create_neurons(neuron_count)
        self.layer_type = layer_type

        self.layer_output_pattern = Pattern(initialize_zero_results(neuron_count), [], '') # Blank pattern used to store fire results and weights of neurons in this layer

        # Neuron weights for this (self) layer
        self.layer_weights = self.generate_random_weights(neuron_count)
        self.layer_value = -1.0
        self.layer_value_weight = random.random() - 0.45

    def initialize_zero_results(self, neuron_count):
        initial_output = []
        for i in range(0, neuron_count):
            initial_output.append(0)

        return initial_output
    
    def generate_random_weights(self, count):
        weights = []
        for i in range(0, count):
            weights.append(random.random() - 0.45)

        return weights

    def create_neurons(self, neuron_count):
        neurons = []
        for i in range(0, neuron_count):
            neurons.append(Neuron())

        return neurons

    def fire_layer(self, input_pattern):
        fire_results = []
        for neuron in self.neurons:
            fire_results.append(neuron.fire(input_pattern))

        self.layer_output_pattern.vector = fire_results
        return self.layer_output_pattern





