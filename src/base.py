import database.database as db
import numpy as npy
import matplotlib.pyplot as plt

def show_img(id, table):
    # 获取数据
    img = table.select_where_id(id)
    img_data = npy.frombuffer(img[0][1], dtype=npy.uint8)
    img_data.resize((28, 28))

    # 开始绘制
    plt.imshow(255-img_data, cmap='gray', vmin=0, vmax=255)
    plt.colorbar()
    plt.show()

class NeuralLayer:
    def __init__(self, total, last_layer):
        """
        本层的激活值
        本层的偏置
        本层与上一层的权重
        """
        self.total = total
        self.last_layer = last_layer

        self.a = npy.array(total, dtype=npy.float32)
        self.b = npy.array(total, dtype=npy.float32)
        if last_layer is not None:
            self.w = npy.array((total, last_layer.total), dtype=npy.float32)

    def execute(self):
        self.a = self.w * self.last_layer.a + self.b

class NeuralNetwork:
    def __init__(self):
        self.w

    def execute(self, input):
        pass


if __name__=="__main__":
    show_img(100, db.train_table)
    show_img(200, db.train_table)
    show_img(300, db.train_table)
    show_img(400, db.train_table)
