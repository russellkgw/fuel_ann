import random
class Vector(object):

    def __init__(self, vector_size):
        self.values = self.generate_values_array(vector_size)
        self.weights = self.generate_random_weights(vector_size)

        self.bias_value = -1
        self.bias_weight = random.random() - 0.45

    def generate_values_array(self, size):
        values = []
        for i in range(0, size):
            values.append(0.0)

        return values

    def generate_random_weights(self, size):
        weights = []
        for i in range(0, size):
            weights.append(random.random() - 0.45)

        return weights
    
    def net_weighted_value(self):
        result = 0.0 + self.bias_value * self.bias_weight

        for i in range(0, len(self.values)):
            result += self.values[i] * self.weights[i]

        return result
