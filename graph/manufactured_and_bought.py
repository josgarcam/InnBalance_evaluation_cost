from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np
import datetime


def barras_dobles(bought, manufactured):
    # Obtenemos la posicion de cada etiqueta en el eje de X

    # tamaño de cada barra
    width = 0.7
    axes = 0.2

    fig, ax = plt.subplots()
    if bought.get('B') == None:
        datos = [[round(bought['a'],2), round(bought['b'],2), round(bought['c'],2), round(bought['d'],2), round(bought['e'],2)],
                 [round(manufactured['a'],2), round(manufactured['b'],2), round(manufactured['c'],2), round(manufactured['d'],2), round(manufactured['e'],2)]]

    else:
        datos = [[round(bought.get('B')['a'],2), round(bought.get('B')['b'],2), round(bought.get('B')['c'],2), round(bought.get('B')['d'],2), round(bought.get('B')['e'],2)],
             [round(manufactured.get('M')['a'],2), round(manufactured.get('M')['b'],2), round(manufactured.get('M')['c'],2), round(manufactured.get('M')['d'],2), round(manufactured.get('M')['e'],2)]]


    X = np.arange(0, 10, step=2)
    # Generamos las barras para el conjunto de hombres
    p1 = plt.bar(X + 0.00, datos[0], color="#AFCB1D", width=width)
    p2 = plt.bar(X + width, datos[1], color="#00000066", width=width)
    # plt.bar(X + 2 * width, datos[2], color="#545454", width=width)
    # plt.bar(X + 3 * width, datos[3], color="#86C05E", width=width)
    # plt.bar(X + 4 * width, datos[4], color="black", width=width)
    plt.xticks(X + 0.4, ["Prototype", "100uds", "1000uds", "10000uds", "50000uds"])

    # Añadimos las etiquetas de identificacion de valores en el grafico
    ax.set_ylabel('Unitary cost(€)')
    # ax.set_xticks(x)
    # ax.set_xticklabels(asistencia)
    # Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
    if bought.get('B') == None:
        plt.legend(['Before MOD', 'After MOD'])
    else:
        plt.legend(['Bought components', 'Manufactured components'])
    fig.tight_layout()

    def autolabel(rects):
        """Funcion para agregar una etiqueta con el valor en cada barra"""
        for rect in rects:
            height = rect.get_height()
            plt.annotate('{}'.format(height),
                          xy=(rect.get_x() + rect.get_width() / 2, height),
                          xytext=(0, 0),  # 3 points vertical offset
                          textcoords="offset points",
                          ha='center', va='bottom', color='black', fontweight='bold')

        # Añadimos las etiquetas para cada barra

    autolabel(p1)
    autolabel(p2)

    # Mostramos la grafica con el metodo show()
    plt.grid()
    plt.show()


def barras_simple(bought):
    width = 0.7

    fig, ax = plt.subplots()
    datos = [[round(bought.get('B')['a'], 2), round(bought.get('B')['b'], 2), round(bought.get('B')['c'], 2),
              round(bought.get('B')['d'], 2), round(bought.get('B')['e'], 2)]]

    X = np.arange(0, 10, step=2)
    p1 = plt.bar(X, datos[0], color="#AFCB1D", width=width)

    def autolabel(rects):
        """Funcion para agregar una etiqueta con el valor en cada barra"""
        for rect in rects:
            height = rect.get_height()
            plt.annotate('{}'.format(height),
                          xy=(rect.get_x() + rect.get_width() / 2, height),
                          xytext=(0, 0),  # 3 points vertical offset
                          textcoords="offset points",
                          ha='center', va='bottom', color='black', fontweight='bold')

        # Añadimos las etiquetas para cada barra

    autolabel(p1)

    plt.xticks(X, ["Prototype", "100uds", "1000uds", "10000uds", "50000uds"])

    plt.grid()
    plt.legend(['Bought components'])
    plt.show()