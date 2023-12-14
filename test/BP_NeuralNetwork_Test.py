import src.base as base
import numpy as npy

# network = base.BP_NeuralNetwork([4, 3, 1])
# network.forward([1, 2, 3, 2])
# network.debug()
# network.save('test.xlsx')

network = base.BP_NeuralNetwork('test.xlsx')
network.save('test2.xlsx')

network = base.BP_NeuralNetwork('../res/AI/1213_2153.xlsx')
network.forward(npy.array([1, 2, 3, 4]))
network.backword(npy.array([0.2]))
network.save('../res/AI/1213_2153_before.xlsx')
