import base
import numpy as npy
import time


# network = base.BP_NeuralNetwork([28*28, 16, 16, 10])
# network.save('../res/AI/backup9.xlsx')

network = base.BP_NeuralNetwork('../res/AI/backup9.xlsx')

# show_img(2222, db.train_table)

data_range = (1, 5000)
start = time.time()
stamp = time.time()
for i in range(*data_range):

    img = base.db.train_table.select_where_id(i)
    img_data = npy.frombuffer(img[0][1], dtype=npy.uint8).astype(npy.float32) / 255
    digit = img[0][2]

    network.forward(img_data)

    target = npy.array([0] * 10)
    target[digit] = 1
    network.backword(target)

    # 每两秒钟输出一次训练进度
    now = time.time()
    if now - stamp > 1:
        print(f'训练进度：{i / (data_range[1] - data_range[0]+1) * 100:.4f}%')
        stamp = now

print(f'训练总耗时：{time.time() - start:.2f}s')
network.save(f'../res/AI/backup9-train.xlsx')
