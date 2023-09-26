import mysql
from torchvision.datasets import mnist

# 登录数据库基本信息
database_login = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'handwritten_digits_recognition'
}

class TrainTable:
    def __init__(self):
        # 建立数据库连接
        self.cnx = mysql.connector.connect(**database_login)

        # 创建数据库游标
        self.cursor = self.cnx.cursor()


    def select_all(self):
        # 执行SQL查询
        query = f'select * from train;'
        self.cursor.execute(query)

        # 获取查询结果
        return self.cursor.fetchall()

    def select_where_id(self, id):
        # 执行SQL查询
        query = f'select * from train where id={id};'
        self.cursor.execute(query)

        # 获取查询结果
        return self.cursor.fetchall()


    def insert(self, img, digit):
        """
        :param img 图片的二进制数据
        :param digit 图片对于的数字
        """
        query = f'insert `train` (`image`, `digit`) values (%s, %s);'
        self.cursor.execute(query, (img, digit))

        # 提交结果
        self.cnx.commit()

train_table = TrainTable()

class TestTable:
    def __init__(self):
        # 建立数据库连接
        self.cnx = mysql.connector.connect(**database_login)

        # 创建数据库游标
        self.cursor = self.cnx.cursor()


    def select_all(self):
        # 执行SQL查询
        query = f'select * from test;'
        self.cursor.execute(query)

        # 获取查询结果
        return self.cursor.fetchall()

    def select_where_id(self, id):
        # 执行SQL查询
        query = f'select * from test where id={id};'
        self.cursor.execute(query)

        # 获取查询结果
        return self.cursor.fetchall()


    def insert(self, img, digit):
        """
        :param img 图片的二进制数据
        :param digit 图片对于的数字
        """
        query = f'insert `test` (`image`, `digit`) values (%s, %s);'
        self.cursor.execute(query, (img, digit))

        # 提交结果
        self.cnx.commit()

test_table = TestTable()

def import_into_table(img_path, label_path, table):
    """
    将 MNIST 数据集的 “.idx3-ubyte” 格式的文件数据导入到mysql数据库中
    :param img_path: 图片数据目录
    :param label_path: 标签数据目录
    :param table: 导入到目标数据库
    """
    train_set = (
        mnist.read_image_file(img_path),
        mnist.read_label_file(label_path)
    )
    for i, (img, label) in enumerate(zip(train_set[0], train_set[1])):
        table.insert(img.numpy().tobytes(), int(label))