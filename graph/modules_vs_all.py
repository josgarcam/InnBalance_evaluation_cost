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
    else:
        pass

    if units != 'All':
        fig, (ax1, ax2) = plt.subplots(1, 2)


        fig.set_size_inches(9.38, 7.13)
        fig.suptitle('Mass production rate = '+str(quantity)+ ' units', fontsize=14, fontweight='bold',
                     bbox={'facecolor': 'yellow', 'alpha': 0.5, 'pad': 10})

        ax1.pie([percentage_anode[units], percentage_cathode[units], percentage_thermal[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"})
        ax1.set_title('Before MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

        ax2.pie([percentage_anode_manuforiented[units], percentage_cathode_manuforiented[units], percentage_thermal_manuforiented[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"})
        ax2.set_title('After MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})


    else:
        fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10)) = plt.subplots(5, 2)
        fig.subplots_adjust(hspace=0.7)
        fig.set_figheight(15)
        # *********************************************************
        units = 'a'
        ax1.pie([percentage_anode[units], percentage_cathode[units], percentage_thermal[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        ax1.set_title('Before MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

        ax2.pie([percentage_anode_manuforiented[units], percentage_cathode_manuforiented[units],
                 percentage_thermal_manuforiented[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        ax2.set_title('After MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

        # *********************************************************
        units = 'b'
        ax3.pie([percentage_anode[units], percentage_cathode[units], percentage_thermal[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        # ax3.set_title('Before MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

        ax4.pie([percentage_anode_manuforiented[units], percentage_cathode_manuforiented[units],
                 percentage_thermal_manuforiented[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        # ax4.set_title('After MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})
        # *********************************************************

        # *********************************************************
        units = 'c'
        ax5.pie([percentage_anode[units], percentage_cathode[units], percentage_thermal[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        # ax5.set_title('Before MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

        ax6.pie([percentage_anode_manuforiented[units], percentage_cathode_manuforiented[units],
                 percentage_thermal_manuforiented[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        # ax6.set_title('After MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})
        # *********************************************************

        # *********************************************************
        units = 'd'
        ax7.pie([percentage_anode[units], percentage_cathode[units], percentage_thermal[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        # ax7.set_title('Before MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

        ax8.pie([percentage_anode_manuforiented[units], percentage_cathode_manuforiented[units],
                 percentage_thermal_manuforiented[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        # ax8.set_title('After MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})
        # *********************************************************

        # *********************************************************
        units = 'e'
        ax9.pie([percentage_anode[units], percentage_cathode[units], percentage_thermal[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        # ax7.set_title('Before MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

        ax10.pie([percentage_anode_manuforiented[units], percentage_cathode_manuforiented[units],
                 percentage_thermal_manuforiented[units]], colors=color,
                labels=nombres,
                autopct="%0.1f %%", textprops={'fontsize': 12}, wedgeprops={"linewidth": 0.5, "edgecolor": "k"}, radius=1.58)
        # ax8.set_title('After MOD', fontsize=12, bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})
        # *********************************************************

        # Separacion entre subplots ---> wspace
        # top --> separacion con el título de la gráfica
    plt.subplots_adjust(wspace=0.5, top=0.98)

    if units == 'a':
        plt.savefig('1unit.png')
    elif units == 'b':
        plt.savefig('100units.png')
    elif units == 'c':
        plt.savefig('1000units.png')
    elif units == 'd':
        plt.savefig('10000units.png')
    elif units == 'e':
        plt.savefig('50000units.png')




    plt.show()
