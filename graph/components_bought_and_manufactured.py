import matplotlib.pyplot as plt

def components_bought_and_manufactured(xlabels, bought_data, manufactured_data):

    def autolabel(rects):
        """Funcion para agregar una etiqueta con el valor en cada barra"""
        for rect in rects:
            height = rect.get_height()

            if rect.get_height() != 0:
                plt.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, -15),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', color='white', fontweight='bold')


    fig = plt.figure("")

    ax = fig.add_subplot(1, 2, 2)

    ax.bar(xlabels, list(manufactured_data.values()))
    autolabel(ax.bar(range(len(manufactured_data)), list(manufactured_data.values()), edgecolor='black', color='#009fe3'))
    plt.title("Manufactured components")
    plt.yticks([0, 5, 10, 15, 20])

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.bar(xlabels, list(bought_data.values()))
    plt.yticks([0,5,10,15,20])
    autolabel(ax1.bar(range(len(bought_data)), list(bought_data.values()), edgecolor='black', color='#afcb1d'))
    plt.title("Bought components")


    plt.ylabel('Number of components')
    plt.savefig('Components_per_module_and_type.png')
    plt.show()