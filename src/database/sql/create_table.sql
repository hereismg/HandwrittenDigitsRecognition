create database handwritten_digits_recognition;
use handwritten_digits_recognition;

# 训练数据集
drop table train;
create table train(
    id int primary key auto_increment,
    image longblob comment '图片',
    digit int comment '数字'
);

# 测试数据集
drop table test;
create table test(
    id int primary key auto_increment,
    image longblob comment '图片',
    digit int comment '数字'
);

#

insert train(image, digit) values (binary('123'), 2);

select * from train;