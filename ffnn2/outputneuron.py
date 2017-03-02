import random
import activation

class OutputNeuron(object):

    def __init__(self):
        self.weight = random.random() - 0.45

    def fire(self, input):
        return activation.sigmoid(input)
