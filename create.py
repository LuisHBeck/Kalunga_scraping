from connect import cursor, data_base

def create(table, modelo, price):
    sql = f'''INSERT INTO {table} (modelo, price)
    values
    ("{modelo}", "{price}")'''

    cursor.execute(sql)
    data_base.commit()

def create_table(table):
    sql = f'''create table {table} (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    price varchar(250)
    );'''

    cursor.execute(sql)
    data_base.commit()

def delete_all():
    sql = f'''DROP TABLE IF EXISTS firstpage, nokia, galaxy, moto, multi'''
    cursor.execute(sql)
    data_base.commit()



