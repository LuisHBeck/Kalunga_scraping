from connect import cursor

def read_brand(table):
    sql = f'SELECT * FROM {table}'

    cursor.execute(sql)
    result = cursor.fetchall()
    return result