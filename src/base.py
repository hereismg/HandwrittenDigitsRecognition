import mysql.connector

# 登录数据库基本信息
database_login = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'handwritten_digits_recognition'
}

class TrainMapper:
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

train_mapper = TrainMapper()

class TestMapper:
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

test_mapper = TestMapper()



if __name__=="__main__":
    result = train_mapper.select_where_id(400)
    # 处理查询结果
    for row in result:
        print(row)
