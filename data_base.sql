create database Kalunga;

use Kalunga;

create table firstPage (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    price varchar(250) 
);

create table sansung (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    price varchar(250)
);

create table motorola (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    price varchar(250)
);

create table nokia (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    price varchar(250)
);