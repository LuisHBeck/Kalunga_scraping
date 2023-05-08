from connect import cursor

def read_brand(table):
    sql = f'SELECT * FROM {table}'

    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def read_only_brand(table):
    sql = f'SELECT modelo FROM {table}'

    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def read_price(table):
    sql = f'SELECT price FROM {table}'

    cursor.execute(sql)
    result = cursor.fetchall()
    return result
