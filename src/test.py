import base
import numpy as npy


network = base.BP_NeuralNetwork('../res/AI/backup9-train.xlsx')

img = base.db.train_table.select_where_id(91)
img_data = npy.frombuffer(img[0][1], dtype=npy.uint8).astype(npy.float32) / 255

network.forward(img_data)
network.debug()

print(f'digit: {img[0][2]}')
