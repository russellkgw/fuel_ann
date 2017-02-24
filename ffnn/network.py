from pattern import Pattern
from layer import Layer

class Network(object):

    def __init__(self, patterns):
        self.patterns = patterns

        self.hidden_layer = Layer(20, 'hidden')
        self.output_layer = Layer(5, 'output')

        self.n = 0.01 # Learning rate
        self.training_iterations = 300
    
    def train_network(self):
        for i in range(1, self.training_iterations):
            print 'Training iteration: ' + str(i)

            for pattern in self.patterns:
                hidden_fire_result_pattern = self.hidden_layer.fire_layer(pattern)
                output_fire_results = self.output_layer.fire_layer(hidden_fire_result_pattern)
                # print str(output_fire_results.vector)
