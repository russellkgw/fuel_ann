from pattern import Pattern
from layer import Layer

class Network(object):

    def __init__(self, patterns):
        self.patterns = patterns

        self.input_layer = Layer(26, 'input')
        self.hidden_layer = Layer(5, 'hidden')

        self.training_iterations = 2
    
    def train_network(self):
        for i in range(1, self.training_iterations):
            print 'Training iteration: ' + str(i)

            for pattern in self.patterns:
                self.input_layer.fire_layer()
                self.hidden_layer.fire_layer()

                # print str(output_layer_fire_result.values)
