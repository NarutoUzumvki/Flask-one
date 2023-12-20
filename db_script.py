from db_connection import connection

cursor = connection.cursor()

create_query = """
CREATE TABLE `employees`(
    `Id` INT AUTO_INCREMENT PRIMARY KEY,
    `Name` varchar(25) NOT NULL,
    `Age` int DEFAULT NULL,
    `Phone` varchar(15) DEFAULT NULL,
    `Department` varchar(20) NOT NULL
)"""

# cursor.execute(create_query)

insert_query = """
INSERT INTO employees
    (`Name`, `Age`, `Phone`, `Department`)
    values
        ('john', 25, '9568745831', 'Tech'),
        ('William', 24, '7356894528', 'Tech'),
        ('David', 23, '9756842358', 'Sales'),
        ('Steeve', 27, '7586489235', 'Sales')
"""

# cursor.execute(insert_query)