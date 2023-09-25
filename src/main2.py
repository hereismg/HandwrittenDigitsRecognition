import struct


def read_idx3_ubyte(file_path):
    with open(file_path, 'rb') as file:
        # 读取文件头
        magic_num, num_items, num_rows, num_cols = struct.unpack('>IIII', file.read(16))

        # 打印文件头信息
        print(f"Magic Number: {magic_num}")
        print(f"Number of items: {num_items}")
        print(f"Number of rows: {num_rows}")
        print(f"Number of columns: {num_cols}")

        # 读取数据集
        if magic_num == 2051:  # 图像数据集
            for _ in range(num_items):
                image = []
                for _ in range(num_rows):
                    row = list(struct.unpack('B' * num_cols, file.read(num_cols)))
                    image.append(row)
                # 在这里可以对图像数据进行进一步处理
                # 例如，将image转换为NumPy数组，应用图像处理算法等
                print(image)  # 打印图像数据

        elif magic_num == 2049:  # 标签数据集
            labels = list(struct.unpack('B' * num_items, file.read(num_items)))
            # 在这里可以对标签数据进行进一步处理
            # 例如，统计标签分布，应用机器学习算法等
            print(labels)  # 打印标签数据


# 读取图像数据集示例
read_idx3_ubyte('../res/train-images.idx3-ubyte')

# 读取标签数据集示例
read_idx3_ubyte('../res/train-labels.idx3-ubyte')