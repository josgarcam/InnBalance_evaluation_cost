import matplotlib.pyplot as plt

def modules_vs_all(result_anode, result_cathode, result_thermal, result_all, units, result_anode_manuforiented,
                   result_cathode_manuforiented, result_thermal_manuforiented, result_all_manuforiented):

    percentage_anode = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    percentage_cathode = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    percentage_thermal = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

    for attr, value in result_all.get('All').items():
        percentage_anode[attr] = result_anode.get('Anode')[attr] / result_all.get('All')[attr]
        percentage_cathode[attr] = result_cathode.get('Cathode')[attr] / result_all.get('All')[attr]
        percentage_thermal[attr] = result_thermal.get('Thermal')[attr] / result_all.get('All')[attr]
    print(percentage_anode)
    print(result_anode)

    percentage_anode_manuforiented = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    percentage_cathode_manuforiented = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    percentage_thermal_manuforiented = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

    for attr, value in result_all_manuforiented.get('All').items():
        percentage_anode_manuforiented[attr] = result_anode_manuforiented.get('Anode')[attr] / result_all_manuforiented.get('All')[attr]
        percentage_cathode_manuforiented[attr] = result_cathode_manuforiented.get('Cathode')[attr] / result_all_manuforiented.get('All')[attr]
        percentage_thermal_manuforiented[attr] = result_thermal_manuforiented.get('Thermal')[attr] / result_all_manuforiented.get('All')[attr]

    # print(percentage_anode_manuforiented)
    # print(result_anode_manuforiented)

    color = ['#009fe3', '#AFCB1D', '#545454']
    nombres = ['Anode', 'Cathode', 'Thermal']

    # Esto es para que el título de la gráfica muestre el valor del mass production rate y no las letras (a, ..., e)
    if units == 'a':
        quantity = 1
    elif units == 'b':
        quantity = 100
    elif units == 'c':
        quantity = 1000
    elif units == 'd':
        quantity = 10000
    elif units == 'e':
        quantity = 50000

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Mass production rate = '+str(quantity)+ ' units', fontsize=14, fontweight='bold',
                 bbox={'facecolor': 'yellow', 'alpha': 0.5, 'pad': 10})
    ax1.pie([percentage_anode[units], percentage_cathode[units], percentage_thermal[units]], colors=color,
            labels=nombres,
            autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"})
    ax1.set_title('Before Manufacturing oriented \ndesign', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

    ax2.pie([percentage_anode_manuforiented[units], percentage_cathode_manuforiented[units], percentage_thermal_manuforiented[units]], colors=color,
            labels=nombres,
            autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"})
    ax2.set_title('After Manufacturing oriented \ndesign', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

    # Separacion entre subplots ---> wspace
    # top --> separacion con el título de la gráfica
    plt.subplots_adjust(wspace=0.5, top=0.85)
    plt.show()
