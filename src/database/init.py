import base

# 导入数据
base.import_into_table(
    '../res/t10k-images.idx3-ubyte',
    '../res/t10k-labels.idx1-ubyte',
    base.test_table
)
base.import_into_table(
    '../res/train-images.idx3-ubyte',
    '../res/train-labels.idx1-ubyte',
    base.train_table
)