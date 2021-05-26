import numpy as np
import matplotlib.pyplot as plt_
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter

def barras_apildas(total_cost_manufactured_false, total_cost_manufactured_true):
    manufactured_false = []
    manufactured_false = list(total_cost_manufactured_false.values())

    manufactured_true = []
    manufactured_true = list(total_cost_manufactured_true.values())

    print("manufactured_true ", manufactured_true)

    dif = []
    percentage = []

    for i in range(len(manufactured_true)):
        dif = manufactured_false[i] - manufactured_true[i]
        percentage.append((manufactured_false[i] - manufactured_true[i])/manufactured_false[i])
    ind = np.arange(len(manufactured_true))
    width = 0.35
    # dif = []
    # for i in range(len(b_means)):
    #     dif.append(b_means[i]-a_means[i])
    fig, ax = plt_.subplots()
    fig.set_size_inches(7.38, 6.13)
    p1 = plt_.bar(ind, manufactured_false, width, color = '#3498db')
    p2 = plt_.bar(ind, dif, width, bottom=manufactured_false, color = '#f8c471')

    plt_.ylabel('Unitary cost [€]')
    plt_.xlabel('Number of Produced Units')

    plt_.xticks(ind, ["Prototype", "100uds", "1,000uds", "10,000uds", "50,000uds"])
    plt_.grid(lw = 0.1)

    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt_.legend(['No MOD', 'MOD'])
    fig.set_size_inches(7.38, 6.13)
    fig.savefig('barras_apiladas.png', bbox_inches="tight")
    print("Con bought components ", percentage)

    plt_.show()


def barras_apildas_sin_bought_components(total_cost_manufactured_false, total_cost_manufactured_true):
    manufactured_false = []
    manufactured_false = list(total_cost_manufactured_false['M'].values())

    manufactured_true = []
    manufactured_true = list(total_cost_manufactured_true['M'].values())

    fig, ax = plt_.subplots()
    fig.set_size_inches(7.38, 6.13)

    dif = []
    percentage = []

    for i in range(len(manufactured_true)):
        dif.append(manufactured_false[i] - manufactured_true[i])
        percentage.append((manufactured_false[i] - manufactured_true[i])/manufactured_false[i])
    ind = np.arange(len(manufactured_true))
    width = 0.35
    # dif = []
    # for i in range(len(b_means)):
    #     dif.append(b_means[i]-a_means[i])
    p1 = plt_.bar(ind, manufactured_false, width, color = '#3498db')
    p2 = plt_.bar(ind, dif, width, bottom=manufactured_false, color = '#f8c471')

    plt_.ylabel('Unitary cost [€]')
    plt_.xlabel('Number of Produced Units')

    plt_.xticks(ind, ["Prototype", "100uds", "1,000uds", "10,000uds", "50,000uds"])
    plt_.grid(lw = 0.1)

    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt_.legend(['No MOD', 'MOD'])
    fig.set_size_inches(7.38, 6.13)
    fig.savefig('barras_apiladas_sin_bought.png', bbox_inches="tight")


    plt_.show()
    print("Percentage Sin bought components", percentage)
