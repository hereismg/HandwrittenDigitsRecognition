create database handwritten_digits_recognition;
use handwritten_digits_recognition;

create table train(
    id int primary key auto_increment,
    image longblob comment '图片',
    digit int comment '数字'
);
drop table train;

create table test(
    id int primary key auto_increment,
    image longblob comment '图片',
    digit int comment '数字'
);
drop table test;

insert train(image, digit) values (2021, 2);

select * from train;