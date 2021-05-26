from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np
import datetime
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter


def barras_dobles(bought, manufactured, mod):
    # Obtenemos la posicion de cada etiqueta en el eje de X

    # tamaño de cada barra
    width = 0.7
    axes = 0.2

    fig, ax = plt.subplots()
    fig.set_size_inches(7.38, 6.13)
    if bought.get('B') == None:
        datos = [[int(bought['a']), int(bought['b']), int(bought['c']), int(bought['d']), int(bought['e'])],
                 [int(manufactured['a']), int(manufactured['b']), int(manufactured['c']), int(manufactured['d']), int(manufactured['e'])]]

    else:
        datos = [[int(bought.get('B')['a']), int(bought.get('B')['b']), int(bought.get('B')['c']), int(bought.get('B')['d']), int(bought.get('B')['e'])],
             [int(manufactured.get('M')['a']), int(manufactured.get('M')['b']), int(manufactured.get('M')['c']), int(manufactured.get('M')['d']), int(manufactured.get('M')['e'])]]

    print(datos)
    X = np.arange(0, 10, step=2)
    # Generamos las barras para el conjunto de hombres
    p1 = plt.bar(X + 0.00, datos[0], color="#AFCB1D", width=width)
    p2 = plt.bar(X + width, datos[1], color="#00000066", width=width)
    # plt.bar(X + 2 * width, datos[2], color="#545454", width=width)
    # plt.bar(X + 3 * width, datos[3], color="#86C05E", width=width)
    # plt.bar(X + 4 * width, datos[4], color="black", width=width)
    plt.xticks(X + 0.4, ["Prototype", "100uds", "1,000uds", "10,000uds", "50,000uds"])

    # Añadimos las etiquetas de identificacion de valores en el grafico
    ax.set_ylabel('Unitary cost [€]')

    # ax.set_xticks(x)
    # ax.set_xticklabels(asistencia)
    # Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
    if bought.get('B') == None:
        plt.legend(['Before MOD', 'After MOD'])
    else:
        plt.legend(['Bought components', 'Manufactured components'])
    fig.tight_layout()
    plt.xlabel('Number of Produced Units')

    def autolabel(rects):
        """Funcion para agregar una etiqueta con el valor en cada barra"""
        for rect in rects:
            height = rect.get_height()
            plt.annotate('{}'.format(height),
                          xy=(rect.get_x() + rect.get_width() / 2, height),
                          xytext=(0, 0),  # 3 points vertical offset
                          textcoords="offset points",
                          ha='center', va='bottom', color='black', fontweight='bold', rotation=0)

        # Añadimos las etiquetas para cada barra

    autolabel(p1)
    autolabel(p2)

    # plt.ylim(0, 2200)

    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    # Mostramos la grafica con el metodo show()
    plt.grid(lw=0.1)
    if mod == str(False):
        fig.savefig('Manufactured_and_bought_MOD_False.png', bbox_inches="tight")
    elif mod == str(True):
        fig.savefig('Manufactured_and_bought_MOD_True.png', bbox_inches="tight")
    else:
        fig.savefig('Manufacturado_vs_bought.png', bbox_inches="tight")


    plt.show()

def barras_simple(bought):
    width = 0.7

    fig, ax = plt.subplots()
    datos = [[round(bought.get('B')['a']), round(bought.get('B')['b']), round(bought.get('B')['c']),
              round(bought.get('B')['d']), round(bought.get('B')['e'])]]

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

    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax.set_ylabel('Unitary cost [€]')
    autolabel(p1)
    plt.xlabel('Number of Produced Units')
    plt.xticks(X, ["Prototype", "100uds", "1,000uds", "10,000uds", "50,000uds"])

    plt.grid(lw=0.1)
    plt.legend(['Bought components'])
    plt.show()