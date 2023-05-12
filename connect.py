import mysql.connector

data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='kalunga3'
)

cursor = data_base.cursor()