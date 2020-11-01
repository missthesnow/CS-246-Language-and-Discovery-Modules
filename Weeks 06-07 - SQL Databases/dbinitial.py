import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
        first text,   
        last text,          
        pay integer
        )""")
        
conn.close()