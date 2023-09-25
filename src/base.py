import mysql.connector

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


    def insert(self, img: str, digit: int):
        """
        :param img 图片的二进制数据
        :param digit 图片对于的数字
        """
        query = f'insert train(image, digit) values ({img}, {digit});'
        self.cursor.execute(query)

        # 提交结果
        self.cnx.commit()


if __name__=="__main__":
    train_table = TrainMapper()

    train_table.insert('222222', 33)

    result = train_table.select_all()
    # 处理查询结果
    for row in result:
        print(row)
