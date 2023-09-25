import os
from base import train_mapper
from base import test_mapper
from skimage import io
import torchvision.datasets.mnist as mnist

def convert_to_img(img_path, label_path):
    train_set = (
        mnist.read_image_file(img_path),
        mnist.read_label_file(label_path)
    )
    for i, (img, label) in enumerate(zip(train_set[0], train_set[1])):
        test_mapper.insert(img.numpy().tobytes(), int(label))


# convert_to_img('../res/train-images.idx3-ubyte')  # 转换训练集
convert_to_img(
    '../res/t10k-images.idx3-ubyte',
    '../res/train-labels.idx1-ubyte'
)