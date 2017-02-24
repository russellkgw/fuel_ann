class Vector(object):

    def __init__(self, size):
        self.values = self.generate_random_values(size)
        self.weights = self.generate_random_values(size)

        self.bias_value = -1
        self.bias_weight = random.random() - 0.45

    def generate_random_values(self, size):
        weights = []
        for i in range(0, size):
            weights.append(random.random() - 0.45)
        
        return weights
