# -*- coding:utf-8 -*-
create_database_info_list = '''CREATE DATABASE `all_info`;'''

create_table_info = '''CREATE TABLE `all_info` (
`id` int not null auto_increment,
`url` varchar(255) not null,
`urlmd5` varchar(100) not null,
`info` text,
`create_time` TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP ,
PRIMARY KEY (`id`),
UNIQUE KEY (`urlmd5`)
) ENGINE=InnoDB CHARSET=utf8;'''