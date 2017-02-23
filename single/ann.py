import random
from neuron import Neuron
from pattern import Pattern

# Vectors
def pattern_array():
    expected_1 = 1.0
    expected_0 = 0.0

    patterns = [Pattern([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1], expected_0, 'A')]

    patterns.insert(1, Pattern([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1] ,expected_1, 'B'))
    patterns.insert(2, Pattern([1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1] ,expected_0, 'C'))
    patterns.insert(3, Pattern([1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0] ,expected_0, 'D'))
    patterns.insert(4, Pattern([1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1] ,expected_0, 'E'))
    patterns.insert(5, Pattern([1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0] ,expected_0, 'F'))
    patterns.insert(6, Pattern([1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1] ,expected_0, 'G'))
    patterns.insert(7, Pattern([1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1] ,expected_0, 'H'))
    patterns.insert(8, Pattern([1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1] ,expected_0, 'I'))
    patterns.insert(9, Pattern([1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0] ,expected_0, 'J'))
    patterns.insert(10, Pattern([1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1] ,expected_0, 'K'))
    patterns.insert(11, Pattern([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1] ,expected_0, 'L'))
    patterns.insert(12, Pattern([1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1] ,expected_0, 'M'))
    patterns.insert(13, Pattern([1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1] ,expected_0, 'N'))
    patterns.insert(14, Pattern([1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1] ,expected_0, 'O'))
    patterns.insert(15, Pattern([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0] ,expected_0, 'P'))
    patterns.insert(16, Pattern([1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1] ,expected_0, 'Q'))
    patterns.insert(17, Pattern([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1] ,expected_0, 'R'))
    patterns.insert(18, Pattern([1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1] ,expected_0, 'S'))
    patterns.insert(19, Pattern([1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0] ,expected_0, 'T'))
    patterns.insert(20, Pattern([1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1] ,expected_0, 'U'))
    patterns.insert(21, Pattern([1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0] ,expected_0, 'V'))
    patterns.insert(22, Pattern([1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1] ,expected_0, 'W'))
    patterns.insert(23, Pattern([1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1] ,expected_0, 'X'))
    patterns.insert(24, Pattern([1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0] ,expected_0, 'Y'))
    patterns.insert(25, Pattern([1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1] ,expected_0, 'Z'))

    return patterns

myNeuron = Neuron(pattern_array())
myNeuron.train_neuron()
myNeuron.eval_neuron(1)