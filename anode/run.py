import pandas as pd
from model.query import data_extraction, labels
from model.operations import sum_labels, sum_origin, sum_manufactured_and_bought
from model.models import Anode
import matplotlib.pyplot as plt
from graph.origin_vs_cost import origin_vs_cost
from graph.labels_vs_cost import labels_vs_cost
from graph.manufactured_vs_bought import manufactured_vs_bought
from graph.manufactured_and_bought import barras_dobles
from graph.manuforiented_true_and_false import barras_apildas, barras_apildas_sin_bought_components


# Son las condiciones para la consulta
query_conditions = {'manuforiented':False, 'origin':'M'}

# Lista de labels que coinciden con los criterios de la consulta (query_conditions)
extracted_labels = []
extracted_labels = labels(Anode, query_conditions)

# Datos extraidos en base a las condiciones de la query
data = data_extraction(Anode, query_conditions, False)

# Costes correspondientes a los test y assemblies
data_test_assembly = data_extraction(Anode, query_conditions, True)

result = sum_labels(data, extracted_labels)
cantidades = ["1", "100", "1000", "10000", "50000"]

# Representar origin vs costes unitarios
# origin_vs_cost(result, cantidades, query_conditions)

# Representar labels vs costes unitarios
# labels_vs_cost(result, cantidades, query_conditions)

# *************** MANUFACTURED vs BOUGHT ****************

data_manufactured = None
data_manufactured = data_extraction(Anode, query_conditions, False)

# Sumatorio de costes, unitarios, para piezas manufacturadas
result_manufactured = sum_origin(data_manufactured, query_conditions)

query_conditions['origin'] = 'B'
data_bought = None
data_bought = data_extraction(Anode, query_conditions, False)

# Sumatorio de costes, unitarios, para piezas compradas
result_bought = sum_origin(data_bought, query_conditions)

# Manuforiented = TRUE
query_conditions = {'manuforiented':True, 'origin':'M'}

data_manufactured_manuforiented_true = None
data_manufactured_manuforiented_true = data_extraction(Anode, query_conditions, False)

# Sumatorio de costes, unitarios, para piezas manufacturadas
result_manufactured_manuforiented_true = sum_origin(data_manufactured_manuforiented_true, query_conditions)

query_conditions['origin'] = 'B'
data_bought_manuforiented_true = None
data_bought_manuforiented_true = data_extraction(Anode, query_conditions, False)

# Sumatorio de costes, unitarios, para piezas compradas
result_bought_manuforiented_true = sum_origin(data_bought_manuforiented_true, query_conditions)

# Costes totales antes del re-design
total_cost_manufactured_false = sum_manufactured_and_bought(result_bought, result_manufactured)
print("result_bought ", result_bought)
print("result_manufactured ", result_manufactured)
print("total_cost_manufactured_false ", total_cost_manufactured_false)
# Costes totales despues del re-design
total_cost_manufactured_true = sum_manufactured_and_bought(result_bought_manuforiented_true, result_manufactured_manuforiented_true)



# Representar % costes piezas compradas vs manufacturadas
# El primer par??metro es los costes que se van a calcular -> a=1uds, ..., e=50000uds
# manufactured_vs_bought('d', result_bought, result_manufactured)

# Representar costes de componentes comprados y manufacturados, en barras paralelas
# barras_dobles(result_bought, result_manufactured)

# Representar costes costes totales, antes y despu??s del manufacturado
# barras_dobles(total_cost_manufactured_false, total_cost_manufactured_true)

# Representar, barras apiladas, manuforiented= False and True
# barras_apildas(total_cost_manufactured_false, total_cost_manufactured_true)



print("Seleccione el tipo de gr??fico:")
print("1- Bought vs manufactured components")
print("2- Manufacturing oriented design - Cost reduction (barras apildas)")
print("3- Bought vs manufactured components (%)")
print("4- Category vs cost")
print("5- Cost before and after manufacturing oriented design")
tipo_grafica = input()


if tipo_grafica == str(1):
    print("Antes (False) o despues(True) del MOD")
    mod = input()
    if mod == str(False):
        barras_dobles(result_bought, result_manufactured, mod)
    if mod == str(True):
        barras_dobles(result_bought_manuforiented_true, result_manufactured_manuforiented_true, mod)


if tipo_grafica == str(2):

    barras_apildas(total_cost_manufactured_false, total_cost_manufactured_true)

    barras_apildas_sin_bought_components(result_manufactured, result_manufactured_manuforiented_true)

if tipo_grafica == str(3):
    print("Antes (False) o despues(True) del MOD")
    mod = input()
    print("Mass Production Rate (MPR) - a, ..., e")
    mpr = input()


    if mod == str(True):
        manufactured_vs_bought(str(mpr), result_bought_manuforiented_true, result_manufactured_manuforiented_true, mod)
    if mod == str(False):
        manufactured_vs_bought(str(mpr), result_bought, result_manufactured, mod)

if tipo_grafica == str(4):
    print("Bought(B) or Manufactured(M)")
    origin = input()
    print("Antes (False) o despues(True) del MOD")
    mod = input()

    query_conditions = {'manuforiented': str(mod), 'origin': origin}
    print("query_conditions ", query_conditions)
    # Lista de labels que coinciden con los criterios de la consulta (query_conditions)
    extracted_labels = []
    extracted_labels = labels(Anode, query_conditions)

    print("extracted_labels ", extracted_labels)

    # Datos extraidos en base a las condiciones de la query
    data = data_extraction(Anode, query_conditions, False)

    result = sum_labels(data, extracted_labels)
    labels_vs_cost(result, cantidades, query_conditions)

if tipo_grafica == str(5):
    query_conditions = {'manuforiented': False}
    data_test_assembly_MOD_false = data_extraction(Anode, query_conditions, True)

    total_cost_manufactured_false['a'] += float(data_test_assembly_MOD_false[0].a)
    total_cost_manufactured_false['b'] += float(data_test_assembly_MOD_false[0].b)
    total_cost_manufactured_false['c'] += float(data_test_assembly_MOD_false[0].c)
    total_cost_manufactured_false['d'] += float(data_test_assembly_MOD_false[0].d)
    total_cost_manufactured_false['e'] += float(data_test_assembly_MOD_false[0].e)


    query_conditions = {'manuforiented': True}
    data_test_assembly_MOD_true = data_extraction(Anode, query_conditions, True)

    total_cost_manufactured_true['a'] += float(data_test_assembly_MOD_true[0].a)
    total_cost_manufactured_true['b'] += float(data_test_assembly_MOD_true[0].b)
    total_cost_manufactured_true['c'] += float(data_test_assembly_MOD_true[0].c)
    total_cost_manufactured_true['d'] += float(data_test_assembly_MOD_true[0].d)
    total_cost_manufactured_true['e'] += float(data_test_assembly_MOD_true[0].e)

    barras_dobles(total_cost_manufactured_false, total_cost_manufactured_true, None)