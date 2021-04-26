

# Calcula la suma, agregacion, agrupado por los labels
def sum_labels(objects, labels):

    result = {}

    for label in labels:
        result[label]={'a':0, 'b':0, 'c':0, 'd':0, 'e':0}
    for obj in objects:
        result[obj.label]['a'] += obj.a
        result[obj.label]['b'] += obj.b
        result[obj.label]['c'] += obj.c
        result[obj.label]['d'] += obj.d
        result[obj.label]['e'] += obj.e

    # result = pd.DataFrame.from_dict(result)
    return result


# Calcula la suma, agregacion, agrupado por el origin (Bought o Manufactured)
def sum_origin(objects, query_conditions):
    result = {}

    result[query_conditions.get('origin')] = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    for obj in objects:
        if obj.a != None:
            result[query_conditions.get('origin')]['a'] += obj.a
            result[query_conditions.get('origin')]['b'] += obj.b
            result[query_conditions.get('origin')]['c'] += obj.c
            result[query_conditions.get('origin')]['d'] += obj.d
            result[query_conditions.get('origin')]['e'] += obj.e

    return result

# Calcula la suma, agregacion, agrupado por el modulo (anodo, catodo, thermal)
def sum_module(objects, component):
    result = {}

    result[component] = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    for obj in objects:
        result[component]['a'] += obj.a
        result[component]['b'] += obj.b
        result[component]['c'] += obj.c
        result[component]['d'] += obj.d
        result[component]['e'] += obj.e

    return result

def sum_manufactured_and_bought(result_bought, result_manufactured):
    result = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

    result['a'] = result_manufactured.get('M')['a'] + result_bought.get('B')['a']
    result['b'] = result_manufactured.get('M')['a'] + result_bought.get('B')['b']
    result['c'] = result_manufactured.get('M')['a'] + result_bought.get('B')['c']
    result['d'] = result_manufactured.get('M')['a'] + result_bought.get('B')['d']
    result['e'] = result_manufactured.get('M')['a'] + result_bought.get('B')['e']

    return result

def components_based_on_origin(data_anode, data_cathode, data_thermal):
    bought_components = {'Anode': 0, 'Cathode': 0, 'Thermal': 0}
    manufactured_components = {'Anode': 0, 'Cathode': 0, 'Thermal': 0}

    for dat in data_anode:
        if dat.origin == 'B':
            bought_components['Anode'] += 1
        elif dat.origin == 'M':
            manufactured_components['Anode'] += 1

    for dat in data_cathode:
        if dat.origin == 'B':
            bought_components['Cathode'] += 1
        elif dat.origin == 'M':
            manufactured_components['Cathode'] += 1

    for dat in data_thermal:
        if dat.origin == 'B':
            bought_components['Thermal'] += 1
        elif dat.origin == 'M':
            manufactured_components['Thermal'] += 1

    return bought_components, manufactured_components
