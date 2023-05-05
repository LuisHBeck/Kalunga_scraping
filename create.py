from connect import cursor, data_base

def create(table, modelo, price):
    sql = f'''INSERT INTO {table} (modelo, price)
    values
    ("{modelo}", "{price}")'''

    cursor.execute(sql)
    data_base.commit()
