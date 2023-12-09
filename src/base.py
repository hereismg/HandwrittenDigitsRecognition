import database.database as db
import numpy as npy
import matplotlib.pyplot as plt
import openpyxl as xl
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
    def __init__(self, last_total=1, current_total=1):
        """
        :param last_total    前一层的神经元的总数量
        :param current_total 这一层的神经元的总数量
        """
        self.current_total = current_total
        self.last_total = last_total

        # A：激活值表
        # B：偏置表
        # W：权重表
        self._A = npy.zeros(current_total, dtype=npy.float32)
        self._B = npy.zeros(current_total, dtype=npy.float32)
        self._W = npy.zeros((last_total, current_total), dtype=npy.float32)

    def execute(self, A_last: npy.ndarray):
        """
        根据给定的前一层神经元的激活值改变该层神经元的激活值
        :param A_last: 前一层神经元的激活值
        :return: 无返回值
        """
        if len(A_last) != self._W.shape[0]:
            print("NeuralLayer::execute(): 输入神经元和本层神经元总数不相等！")
        self._A = self._W * A_last + self._B

    def set_A(self, A):
        if len(A) != len(self._A):
            print("NeuralLayer::set_A(): 尺寸不相符！")
        self._A = A

    def load(self, sheet):
        """
        读取数据表中的数据
        :param sheet: 工作表对象。注意不是传入excel，而是sheet
        """
        data = [[cell.value for cell in row] for row in sheet.rows]
        self._W = npy.array([row for row in data[:-2]])
        self._B = npy.array(data[-2])
        self._A = npy.array(data[-1])

        self.last_total = self._W.shape[0]
        self.current_total = self._W.shape[1]

    def save(self, sheet):
        """
        将该层神经网络存储到对于的 excel 表格中。
        在将数据存入到 excel 中，为了方便计算，写入的顺序是：W、B、A ！！！
        :param sheet: 工作表对象。注意不是传入excel，而是sheet
        """
        for item in self._W:
            sheet.append(list(item))
        sheet.append(list(self._B))
        sheet.append(list(self._A))


class NeuralNetwork:
    def __init__(self):
        self.size = [0, 28*28, 16, 16, 10]
        self.network = [NeuralLayer(self.size[i], self.size[i+1]) for i in range(len(self.size)-1)]

    def execute(self, input):
        """
        根据输入的参数，运行神经网络。
        注意：输入值应该是一个竖向量
        :param input: 输入参数，这是一个竖向量
        """
        self.network[0].set_A(input)
        for i in range(1, len(self.network)):
            self.network[i].execute(self.network[i-1]._A)

    def debug(self):
        """
        打印神经网络的结果
        """
        print('[', end='')
        for i in range(self.size[-1] - 1):
            print(f'{self.network[-1]._A[i]},\t', end='')
        print(f'{self.network[-1]._A[-1]}]')

    def save(self, file):
        wb = xl.Workbook()

        number = 1
        for layer in self.network[1:]:
            ws = wb.create_sheet(f'layer{number}')
            layer.save(ws)
            number += 1

        # wb.remove('Sheet')
        wb.save(file)


if __name__=="__main__":
    # wb = load_workbook('../res/Template.xlsx')
    # sheet = wb['layer1']
    # sheet['A1'] = '2021'
    # sheet['A2'] = '=A1'
    # wb.save("../ai/out.xlsx")

    # file_paht = '../res/Template.xlsx'
    # data_frame = pd.read_excel(file_paht)

    # show_img(444, db.train_table)

    # network = NeuralNetwork()
    # network.save('backup.xlsx')

    # wb = xl.Workbook()
    # ws = wb.create_sheet('first')
    #
    # layer = NeuralLayer(10, 5)
    # layer.set_A([1, 2, 3, 4, 5])
    # layer.save(ws)
    # wb.save('backup.xlsx')

    wb = xl.load_workbook('backup.xlsx')

    layer = NeuralLayer()
    layer.load(wb['layer1'])


    layer.save(wb.create_sheet('newsheet'))
    wb.save('new.xlsx')