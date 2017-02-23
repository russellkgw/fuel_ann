import random

class Pattern(object):

    def __init__(self, vector, target_value, letter):
        self.vector = vector
        self.weights = self.generate_random_weights(len(self.vector))

        self.target_value = target_value
        self.letter = letter

        self.bias_value = -1.0
        self.bias_weight = random.random() - 0.45

    def generate_random_weights(self, length):
        weights = []
        for i in range(0, length - 1):
            weights.insert(i, random.random() - 0.45)

        return weights
