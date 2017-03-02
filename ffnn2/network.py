from pattern import Pattern
from vector import Vector
from inputlayer import InputLayer
from hiddenlayer import HiddenLayer
from outputlayer import OutputLayer

class Network(object):

    def __init__(self, patterns):
        self.patterns = patterns
                                                # |||||||||||||||||||||||||
        self.input_layer = InputLayer(25)       # 0000000000000000000000000     one neuron per input unit
        self.input_layer_output = Vector(25)    # |||||||||||||||||||||||||B    one output per neuron and bias
        self.hidden_layer = HiddenLayer(20)     #    00000000000000000000       send net output value to layer to be fired by neurons
        self.hidden_layer_output = Vector(20)   #    ||||||||||||||||||||B      one output per neuron and bias
        self.output_layer = OutputLayer(5)      #            00000              send net output value to layer to be fired by output layer
        self.output_layer_output = Vector(5)    #            |||||

        self.training_iterations = 2

    def train_network(self):
        # set training here

        for pattern in self.patterns:
            self.input_layer_output.values = self.input_layer.fire_input_layer(pattern.vector)
            self.hidden_layer_output.values = self.hidden_layer.fire_hidden_layer(self.input_layer_output.net_weighted_value())
            self.output_layer_output.values = self.output_layer.fire_output_layer(self.hidden_layer_output.net_weighted_value())
            print str(self.output_layer_output.values)
