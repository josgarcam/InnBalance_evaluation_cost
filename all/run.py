from model.models import Anode, Cathode, Thermal
from model.query import data_extraction
from model.operations import sum_module, components_based_on_origin
from graph.components_bought_and_manufactured import components_bought_and_manufactured
from graph.modules_vs_all import modules_vs_all
from graph.modules_vs_cost import barras_paralelas

# Units --> a=1, ..., e=50000
units='e'

# Son las condiciones para la consulta - MANUFORIENTED = FALSE
query_conditions = {'manuforiented':False}

# Datos extraidos en base a las condiciones de la query
# data_anode --> contendrá todos los datos del anodo, componetes y costes
data_anode = data_extraction(Anode, query_conditions)
data_cathode = data_extraction(Cathode, query_conditions)
data_thermal = data_extraction(Thermal, query_conditions)

result_anode = sum_module(data_anode, 'Anode')
result_cathode = sum_module(data_cathode, 'Cathode')
result_thermal = sum_module(data_thermal, 'Thermal')

result_all = {'All': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}}
for attr, value in result_anode.get('Anode').items():
    result_all.get('All')[attr] = result_anode.get('Anode')[attr] + result_cathode.get('Cathode')[attr] +\
                                  result_thermal.get('Thermal')[attr]


# Son las condiciones para la consulta - MANUFORIENTED = TRUE
query_conditions = {'manuforiented':True}


# Datos extraidos en base a las condiciones de la query
# data_anode --> contendrá todos los datos del anodo, componetes y costes
data_anode_manuforiented = data_extraction(Anode, query_conditions)
data_cathode_manuforiented = data_extraction(Cathode, query_conditions)
data_thermal_manuforiented = data_extraction(Thermal, query_conditions)

result_anode_manuforiented = sum_module(data_anode_manuforiented, 'Anode')
result_cathode_manuforiented = sum_module(data_cathode_manuforiented, 'Cathode')
result_thermal_manuforiented = sum_module(data_thermal_manuforiented, 'Thermal')


result_all_manuforiented = {'All': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}}

for attr, value in result_anode_manuforiented.get('Anode').items():
    result_all_manuforiented.get('All')[attr] = result_anode_manuforiented.get('Anode')[attr] + result_cathode_manuforiented.get('Cathode')[attr] +\
                                  result_thermal_manuforiented.get('Thermal')[attr]


print("Seleccione el tipo de gráfico:")
print("1- Nº of Bought and manufactured components per module")
print("2- Cost (%) per module base on mass production rate")
print("3- Cost per module based on mass production rate")

tipo_grafica = input()

if tipo_grafica == str(1):
    print("Antes (False) o despues(True) del MOD")
    mod = input()
    if mod == str(False):
        number_bought_components = components_based_on_origin(data_anode, data_cathode, data_thermal)[0]
        number_manufactured_components = components_based_on_origin(data_anode, data_cathode, data_thermal)[1]

        components_bought_and_manufactured(list(number_manufactured_components.keys()), number_bought_components,
                                           number_manufactured_components)
    elif mod == str(True):
        number_bought_components_manuforiented = components_based_on_origin(data_anode_manuforiented, data_cathode_manuforiented, data_thermal_manuforiented)[0]
        number_manufactured_components_manuforiented = components_based_on_origin(data_anode_manuforiented, data_cathode_manuforiented, data_thermal_manuforiented)[1]

        components_bought_and_manufactured(list(number_manufactured_components_manuforiented.keys()), number_bought_components_manuforiented,
                                           number_manufactured_components_manuforiented)

if tipo_grafica == str(2):
    print("Mass Production Rate (MPR) - a, ..., e")
    mpr = (input())

    modules_vs_all(result_anode, result_cathode, result_thermal, result_all, mpr, result_anode_manuforiented,
                   result_cathode_manuforiented, result_thermal_manuforiented, result_all_manuforiented)



if tipo_grafica == str(3):
    print("Antes (False) o despues(True) del MOD")
    mod = input()
    if mod == str(True):
        barras_paralelas(result_anode_manuforiented, result_cathode_manuforiented, result_thermal_manuforiented)
    else:
        barras_paralelas(result_anode, result_cathode, result_thermal)
