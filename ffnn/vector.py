import random

class Vector(object):

    def __init__(self, input_values):
        self.values = input_values
        self.weights = self.generate_random_values(len(input_values))

        self.bias_value = -1
        self.bias_weight = random.random() - 0.45

    def generate_random_values(self, size):
        weights = []
        for i in range(0, size):
            weights.append(random.random() - 0.45)

        return weights

    @staticmethod
    def generate_blank_values(size):
        values = []
        for i in range(0, size):
            values.append(0)

        return values
