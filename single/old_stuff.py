alphabet = [[1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]]
    alphabet.insert(1, [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1])
    alphabet.insert(2, [1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1])
    alphabet.insert(3, [1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0])
    alphabet.insert(4, [1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1])
    alphabet.insert(5, [1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0])
    alphabet.insert(6, [1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1])
    alphabet.insert(7, [1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1])
    alphabet.insert(8, [1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1])
    alphabet.insert(9, [1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0])
    alphabet.insert(10, [1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1])
    alphabet.insert(11, [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1])
    alphabet.insert(12, [1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1])
    alphabet.insert(13, [1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1])
    alphabet.insert(14, [1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1])
    alphabet.insert(15, [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0])
    alphabet.insert(16, [1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1])
    alphabet.insert(17, [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1])
    alphabet.insert(18, [1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1])
    alphabet.insert(19, [1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0])
    alphabet.insert(20, [1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1])
    alphabet.insert(21, [1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0])
    alphabet.insert(22, [1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1])
    alphabet.insert(23, [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1])
    alphabet.insert(24, [1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0])
    alphabet.insert(25, [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1])

myNeuron = Neuron(alphabet_array())
myNeuron.train_neuron(0)
myNeuron.eval_neuron(0)