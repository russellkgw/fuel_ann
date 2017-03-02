import random
from vector import Vector

class Pattern(object):

    def __init__(self, input_vector, target, letter):
        self.vector = input_vector

        self.target_value = target
        self.letter = letter
    