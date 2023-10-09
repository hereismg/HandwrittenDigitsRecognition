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
    """
    神经层
    """
    def __init__(self, total, last_layer=None):
        """
        :param total 该神经层的神经元的总数量
        :param last_layer 上一层神经层
        """
        self.total = total
        self.last_layer = last_layer

        # a：激活值表
        # b：偏置表
        # w：权重表
        self.a = npy.zeros(total, dtype=npy.float32)
        self.b = npy.zeros(total, dtype=npy.float32)
        if last_layer is not None:
            self.w = npy.zeros((total, last_layer.total), dtype=npy.float32)

    def set_last_layer(self, last_layer):
        self.last_layer = last_layer
        self.w = npy.zeros((self.total, last_layer.total), dtype=npy.float32)

    def execute(self):
        self.a = self.w * self.last_layer.a + self.b


class NeuralNetwork:
    def __init__(self):
        self.network = [NeuralLayer(762), NeuralLayer(16), NeuralLayer(16), NeuralLayer(10)]
        for i in range(1, len(self.network)):
            self.network[i].set_last_layer(self.network[i-1])


    def execute(self, input):
        pass


if __name__=="__main__":
    network = NeuralNetwork()
    print(network.__dict__)

