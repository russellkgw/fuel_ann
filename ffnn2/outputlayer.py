from outputneuron import OutputNeuron

class OutputLayer(object):

    def __init__(self, num_neurons):
        self.output_neurons = self.create_output_neurons(num_neurons)

    def create_output_neurons(self, neuron_count):
        neurons = []
        for i in range(0, neuron_count):
            neurons.append(OutputNeuron())

        return neurons

    # Fire each neuron in the list wrt the input
    def fire_output_layer(self, input):
        fire_results = []

        for neuron in self.output_neurons:
            fire_results.append(neuron.fire(input))

        return fire_results