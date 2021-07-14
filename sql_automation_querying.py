import datetime
import mysql.connector

cnx = mysql.connector.connect(user='test1', password='Password.123', database='SiPbxDomain')
cursor = cnx.cursor(buffered=True)

table_list:list = ['employees;', 'departments;', 'salaries;', 'dept_emp;', 'dept_manager;', 'titles;']

for t in table_list:

    query_string = "SELECT * FROM" + ' ' + t
    query = (query_string)
    cursor.execute(query)
    
    print(cursor.column_names)
    print(cursor.fetchall())
    print('*******************************************')
    print('*******************************************')
    print('*******************************************')
    print('*******************************************')
    print('*******************************************')

cursor.close()
cnx.close()
