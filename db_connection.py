import pymysql

db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'SQLP@ssw0rd',
    'database' : 'employee_data',
    'autocommit' : 'True',
}

connection = pymysql.connect(**db_config)