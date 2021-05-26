import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter

def manufactured_vs_bought(units, result_bought, result_manufactured,mod):
    # Calcular el total de precios, manufacturados y comprados
    # result_total alamacenará Manufactured + Bought
    result_total = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

    for attr, value in result_bought.get('B').items():
        result_total[attr] += value

    for attr, value in result_manufactured.get('M').items():
        result_total[attr] += value

    percentage_bought = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    percentage_manufactured = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

    for attr, value in result_total.items():
        percentage_bought[attr] = int(round(result_bought.get('B')[attr] / result_total[attr],2)*100)
        percentage_manufactured[attr] = int(round(result_manufactured.get('M')[attr] / result_total[attr],2)*100)
    print(result_bought.get('B')['a'] / result_total['a'])
    print(percentage_manufactured)
    print(percentage_bought)
    color = ['#AFCB1D', '#00000066']
    nombres = ['Bought components', 'Manufactured components']

    fig, ax = plt.subplots()
    fig.set_size_inches(7.38, 6.13)

    if units != 'ALL':
        plt.pie([percentage_bought[units], percentage_manufactured[units]], colors=color, labels=nombres, autopct="%d %%"
            , explode=[0, 0.05])
    else:
        ax1 = plt.subplot2grid(shape=(2, 6), loc=(0, 0), colspan=2)
        ax2 = plt.subplot2grid((2, 6), (0, 2), colspan=2)
        ax3 = plt.subplot2grid((2, 6), (0, 4), colspan=2)
        ax4 = plt.subplot2grid((2, 6), (1, 1), colspan=2)
        ax5 = plt.subplot2grid((2, 6), (1, 3), colspan=2)


        ax1.pie([percentage_bought['a'], percentage_manufactured['a']], colors=color, autopct="%d %%", explode=[0, 0.05])
        ax1.set_title("Prototype", fontsize=16, fontstyle='italic')

        ax2.pie([percentage_bought['b'], percentage_manufactured['b']], colors=color, autopct="%d %%", explode=[0, 0.05])
        ax2.set_title("100 units", fontsize=16, fontstyle='italic')

        ax3.pie([percentage_bought['c'], percentage_manufactured['c']], colors=color, autopct="%d %%", explode=[0, 0.05])
        ax3.set_title("1,000 units", fontsize=16, fontstyle='italic')

        ax4.pie([percentage_bought['d'], percentage_manufactured['d']], colors=color, autopct="%d %%", explode=[0, 0.05])
        ax4.set_title("10,000 units", fontsize=16, fontstyle='italic')

        ax5.pie([percentage_bought['e'], percentage_manufactured['e']], colors=color, autopct="%d %%"
                , explode=[0, 0.05])
        ax5.set_title("50,000 units", fontsize=16, fontstyle='italic')

        ax5.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

        plt.legend(bbox_to_anchor=(1.1, 1.05), labels=nombres)
    plt.show()
    if mod == str(True):
        fig.savefig('Tarta_Si_MOD.png', bbox_inches="tight")
    if mod == str(False):
        fig.savefig('Tarta_No_MOD.png', bbox_inches="tight")