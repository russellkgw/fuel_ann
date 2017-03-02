from hiddenneuron import HiddenNeuron

class HiddenLayer(object):

    def __init__(self, num_neurons):
        self.hidden_neurons = self.create_hidden_neurons(num_neurons)

    def create_hidden_neurons(self, neuron_count):
        neurons = []
        for i in range(0, neuron_count):
            neurons.append(HiddenNeuron())

        return neurons

    # Fire each neuron in the list wrt the input
    def fire_hidden_layer(self, input):
        fire_results = []

        for neuron in self.hidden_neurons:
            fire_results.append(neuron.fire(input))

        return fire_results
