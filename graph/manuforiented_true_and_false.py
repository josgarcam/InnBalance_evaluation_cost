import numpy as np
import matplotlib.pyplot as plt_

def barras_apildas(total_cost_manufactured_false, total_cost_manufactured_true):
    manufactured_false = []
    manufactured_false = list(total_cost_manufactured_false.values())

    manufactured_true = []
    manufactured_true = list(total_cost_manufactured_true.values())

    dif = []

    for i in range(len(manufactured_true)):
        dif = manufactured_false[i] - manufactured_true[i]

    ind = np.arange(len(manufactured_true))
    width = 0.35
    # dif = []
    # for i in range(len(b_means)):
    #     dif.append(b_means[i]-a_means[i])
    p1 = plt_.bar(ind, manufactured_false, width, color = 'teal')
    p2 = plt_.bar(ind, dif, width, bottom=manufactured_false, color = 'coral')

    plt_.ylabel('Unitary cost(€)')
    plt_.xlabel('Units')

    plt_.xticks(ind, ["Prototype", "100uds", "1000uds", "10000uds", "50000uds"])
    plt_.grid()



    # plt_.legend()
    plt_.show()
