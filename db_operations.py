from db_connection import connection

cursor = connection.cursor()

def insert(data):
    query = """
    insert into employees(`Name`, `Age`, `Phone`, `Department`)
    values
        (%s, %s, %s, %s)
    """
    cursor.execute(query, data)

def retrieve(id):
    query = """
    select * from employees where `Id` = %s
    """
    cursor.execute(query, id)
    data = cursor.fetchone()
    return data

def update(data):
    query = """
    update employees set `Name`=%s, `Age`=%s, `Phone`=%s,
    `Department`=%s where `Id`=%s
    """
    cursor.execute(query,data)


def remove(id):
    query = """
    delete from employees where `Id`=%s
    """
    cursor.execute(query,id)


