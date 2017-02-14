import random
from neuron import Neuron
from pattern import Pattern

# Vectors
def pattern_array():
    expected_1 = 1
    expected_0 = 0
    
    patterns = [Pattern([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]), expected_0]

    patterns.insert(1, Pattern([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1] ,expected_0))
    patterns.insert(2, Pattern([1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1] ,expected_1))
    patterns.insert(3, Pattern([1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0] ,expected_0))
    patterns.insert(4, Pattern([1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1] ,expected_0))
    patterns.insert(5, Pattern([1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0] ,expected_0))
    patterns.insert(6, Pattern([1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1] ,expected_0))
    patterns.insert(7, Pattern([1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1] ,expected_0))
    patterns.insert(8, Pattern([1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1] ,expected_0))
    patterns.insert(9, Pattern([1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0] ,expected_0))
    patterns.insert(10, Pattern([1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1] ,expected_0))
    patterns.insert(11, Pattern([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1] ,expected_0))
    patterns.insert(12, Pattern([1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1] ,expected_0))
    patterns.insert(13, Pattern([1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1] ,expected_0))
    patterns.insert(14, Pattern([1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1] ,expected_0))
    patterns.insert(15, Pattern([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0] ,expected_0))
    patterns.insert(16, Pattern([1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1] ,expected_0))
    patterns.insert(17, Pattern([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1] ,expected_0))
    patterns.insert(18, Pattern([1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1] ,expected_0))
    patterns.insert(19, Pattern([1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0] ,expected_0))
    patterns.insert(20, Pattern([1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1] ,expected_0))
    patterns.insert(21, Pattern([1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0] ,expected_0))
    patterns.insert(22, Pattern([1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1] ,expected_0))
    patterns.insert(23, Pattern([1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1] ,expected_0))
    patterns.insert(24, Pattern([1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0] ,expected_0))
    patterns.insert(25, Pattern([1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1] ,expected_0))

    return patterns

myNeuron = Neuron(pattern_array())
myNeuron.train_neuron(0)
myNeuron.eval_neuron(0)