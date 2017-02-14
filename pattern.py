import random

class Pattern(object):

    def __init__(self, vector, expected_value):
        self.vector = vector
        self.weights = self.generate_random_weights(len(self.vector))

        self.expected_value = expected_value

        self.bias_value = -1
        self.bias_weight = random.random() - 0.4

    def generate_random_weights(self, length):
        weights = []
        for i in range(0, length - 1):
            weights.insert(i, random.random() - 0.4)

        return length

    def generate_zero_updates(self, length):
        weight_updates = []
        for i in range(0, length - 1):
            weight_updates.insert(i, 0.0)

        return weight_updates