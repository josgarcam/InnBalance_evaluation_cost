from model.query import data_extraction
from model.models import Anode, Cathode, Thermal
import sqlite3

#####
table = 'thermal' #anode, cathode or thermal
#####


def def_val(values):
    values = list(values)
    for i in range(len(values)):
        if values[i] is None:
            values[i] = 0
    return tuple(values)


con = sqlite3.connect('C:/Users/jmgarciac/PycharmProjects/InnBalance_evaluation_cost/db.sqlite3')
cur = con.cursor()

query_conditions = {'manuforiented': None, 'origin': None}
if table == 'anode':
    data = data_extraction(Anode, query_conditions, False)
    for row in data:
        cur.execute("INSERT INTO innbalance_dashboard_data_anode(origin, component, model, uds1, uds100, uds1000, uds10000, uds50000, description, manuforiented, label) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    def_val((row.origin, row.component, row.model, row.a, row.b, row.c, row.d, row.e, row.description, 't' if row.manuforiented else 'f', row.label)))

elif table == 'cathode':
    data = data_extraction(Cathode, query_conditions, False)
    for row in data:
        cur.execute("INSERT INTO innbalance_dashboard_data_cathode(origin, component, model, uds1, uds100, uds1000, uds10000, uds50000, description, manuforiented, estimation, label) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    def_val((row.origin, row.component, row.model, row.a, row.b, row.c, row.d, row.e, row.description, 't' if row.manuforiented else 'f', 't' if row.estimation else 'f', row.label)))


elif table == 'thermal':
    data = data_extraction(Thermal, query_conditions, False)
    for row in data:
        cur.execute("INSERT INTO innbalance_dashboard_data_thermal(origin, component, model, uds1, uds100, uds1000, uds10000, uds50000, description, estimation, manuforiented, label) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    def_val((row.origin, row.component, row.model, row.a, row.b, row.c, row.d, row.e, row.description, 't' if row.estimation else 'f', 't' if row.manuforiented else 'f',  row.label)))

con.commit()
con.close()

