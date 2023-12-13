import src.base as base

# network = base.BP_NeuralNetwork([4, 3, 1])
# network.forward([1, 2, 3, 2])
# network.debug()
# network.save('test.xlsx')

network = base.BP_NeuralNetwork('test.xlsx')
network.save('test2.xlsx')