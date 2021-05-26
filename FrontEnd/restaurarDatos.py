from model.query import data_extraction
from model.models import Anode
import sqlite3

con = sqlite3.connect('C:/Users/jmgarciac/PycharmProjects/InnBalance_evaluation_cost/db.sqlite3')
cur = con.cursor()





cur.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

a = cur.execute("SELECT * FROM employees; ")
print (a)

for row in cur.execute("SELECT * FROM employees; "):
    print(row)

query_conditions = {'manuforiented':None, 'origin': None}
anodeData = data_extraction(Anode, query_conditions, False)

print(len(anodeData))