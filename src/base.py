import database.database as db
import numpy as npy
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import pandas as pd

def show_img(id, table):
    """
    根据指定 ID，寻找数据库中的制定图片并展示出来。
    :param id: 图片 ID
    :param table: 所要寻找的数据表
    :return: 无返回值
    """
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
    def __init__(self, current_total, last_total):
        """
        :param current_total 这一层的神经元的总数量
        :param last_total    前一层的神经元的总数量
        """
        self.current_total = current_total
        self.last_total = last_total

        # A：激活值表
        # B：偏置表
        # W：权重表
        self.A = npy.zeros(current_total, dtype=npy.float32)
        self.B = npy.zeros(current_total, dtype=npy.float32)
        self.W = npy.zeros((last_total, current_total), dtype=npy.float32)

    def execute(self, A_last: npy.ndarray):
        """
        根据给定的前一层神经元的激活值改变该层神经元的激活值
        :param A_last: 前一层神经元的激活值
        :return: 无返回值
        """
        if len(A_last) != self.W.shape[0]: print("NeuralLayer::execute(): 输入神经元和本层神经元总数不相等！")
        self.A = self.W * A_last + self.B

    def save(self, sheet):
        """
        将该层神经网络存储到对于的 excel 表格中
        :param sheet: 工作表对象
        :return:
        """
        pass

class NeuralNetwork:
    def __init__(self):
        self.size = [28*28, 16, 16, 10]
        self.network = [NeuralLayer(self.size[i], self.size[i+1]) for i in range(len(self.size)-1)]

    def execute(self, input):
        pass


if __name__=="__main__":
    # wb = load_workbook('../res/Template.xlsx')
    # sheet = wb['layer1']
    # sheet['A1'] = '2021'
    # sheet['A2'] = '=A1'
    # wb.save("../ai/out.xlsx")

    # file_paht = '../res/Template.xlsx'
    # data_frame = pd.read_excel(file_paht)
    show_img(444, db.train_table)