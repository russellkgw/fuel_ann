import random
import activation

class InputNeuron(object):

    def __init__(self):
        self.weight = random.random() - 0.45

    def fire(self, input):
        return activation.linear(input)
