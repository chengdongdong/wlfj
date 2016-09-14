#!/bin/bash
########################################################################
# File Name: create_sql.sh
# Author: chengdong
# mail: zchengdongdong@gmail.com
# Created Time: Sun 11 Sep 2016 11:57:26 AM CST
########################################################################
mysql -u root -p
CREATE DATABASE testdb;
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'test623';
USE testdb;
GRANT ALL ON testdb.* TO 'testuser'@'localhost';
