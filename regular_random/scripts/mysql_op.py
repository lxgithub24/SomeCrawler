# -*- coding:utf-8 -*-


CREATE_TABLE_GRAPH = '''CREATE TABLE `regular`(
`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
`issue_number` int (11) DEFAULT 0,
`pub_time` TIMESTAMP DEFAULT '2017-09-28 00:00:00',
`total_money` int(11),
`first_prize_count` int(11),
`first_prize_province` VARCHAR (255),
`second_prize_count` int(11),
`col1` int NOT NULL ,
`col2` int NOT NULL ,
`col3` int NOT NULL ,
`col4` int NOT NULL ,
`col5` int NOT NULL ,
`col6` int NOT NULL ,
`col7` int NOT NULL ,
`permutation_order` int (11) NOT NULL DEFAULT 0,
`combination_order` int (11) NOT NULL DEFAULT 0,
`create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB CHARSET=utf8;
'''
