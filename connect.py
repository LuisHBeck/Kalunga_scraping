import mysql.connector

data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='kalunga'
)

cursor = data_base.cursor()