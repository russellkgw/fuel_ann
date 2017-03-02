import random
from inputneuron import InputNeuron

class InputLayer(object):

    def __init__(self, num_neurons):
        self.input_neurons = self.create_input_neurons(num_neurons)

    def create_input_neurons(self, neuron_count):
        neurons = []
        for i in range(0, neuron_count):
            neurons.append(InputNeuron())

        return neurons

    # Fire each neuron in the list wrt the input pattern
    def fire_input_layer(self, input):
        fire_results = []
        for i in range(0, len(input)):
            fire_results.append(self.input_neurons[i].fire(input[i]))

        return fire_results
