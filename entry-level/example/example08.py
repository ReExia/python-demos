#!/usr/bin/python3
import pymysql

mysqlUrl = "192.168.80.131"
mysqlUserName = "mysqladmin"
mysqlPassword = "mysqladmin123"
dbName = "shiro_demo"

db = pymysql.connect(mysqlUrl, mysqlUserName, mysqlPassword, dbName)

cursor = db.cursor()

cursor.execute("select * from permission")

data = cursor.fetchall()

print(data)

db.close()
