from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np
import datetime

def barras_paralelas( result_anode, result_cathode, result_thermal, mod):
    # Obtenemos la posicion de cada etiqueta en el eje de X
    x = np.arange(len(result_cathode.get('Cathode')))
    # tamaño de cada barra
    width = 0.4
    axes = 0.2

    fig, ax = plt.subplots()
    datos = [[result_anode.get('Anode')['a'], result_cathode.get('Cathode')['a'], result_thermal.get('Thermal')['a']],
            [result_anode.get('Anode')['b'], result_cathode.get('Cathode')['b'], result_thermal.get('Thermal')['b']],
            [result_anode.get('Anode')['c'], result_cathode.get('Cathode')['c'], result_thermal.get('Thermal')['c']],
            [result_anode.get('Anode')['d'], result_cathode.get('Cathode')['d'], result_thermal.get('Thermal')['d']],
            [result_anode.get('Anode')['e'], result_cathode.get('Cathode')['e'], result_thermal.get('Thermal')['e']]]
    X = np.arange(0, 6, step=2.5)
    # Generamos las barras para el conjunto de hombres
    plt.bar(X + 0.00, datos[0], color="#AFCB1D", width=width)
    plt.bar(X + width, datos[1], color="#00000066", width=width)
    plt.bar(X + 2*width, datos[2], color="#545454", width=width)
    plt.bar(X + 3*width, datos[3], color="#86C05E", width=width)
    plt.bar(X + 4*width, datos[4], color="black", width=width)
    plt.xticks(X + 0.75, ["Anode", "Cathode", "Thermal"])
    plt.grid()
    # Añadimos las etiquetas de identificacion de valores en el grafico
    ax.set_ylabel('Unitary cost(€)')
    # ax.set_xticks(x)
    # ax.set_xticklabels(asistencia)
    # Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
    plt.legend(['1 ud','100 uds', '1000 uds', '10000 uds', '50000 uds'])


    fig.tight_layout()
    fig.set_size_inches(9.38, 7.13)

    if mod == str(False):
        print("before")
        plt.savefig('Before_MOD.png')
    else:

        plt.savefig('After_MOD.png')

    plt.show()
