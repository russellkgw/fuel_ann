import random
from vector import Vector

class Pattern(object):

    def __init__(self, input, target, letter):
        self.vector = input

        self.target_value = target
        self.letter = letter
    