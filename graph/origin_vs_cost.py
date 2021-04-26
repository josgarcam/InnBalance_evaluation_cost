import matplotlib.pyplot as plt
import pandas as pd

def origin_vs_cost(result, cantidades, query_conditions):

    df = pd.DataFrame(data=result).transpose()
    df.plot(rot=20, kind='bar', color=['#AFCB1D', '#00000066', '#545454', '#86C05E', 'black'])

    plt.grid()
    # pd.DataFrame()

    if query_conditions.get('origin') == 'B':
        if query_conditions.get('manuforiented') == False:
            plt.xlabel('Bought components', fontsize=12)
        else:
            plt.xlabel('Bought components', fontsize=12)
    else:
        if query_conditions.get('manuforiented') == True:
            plt.xlabel('Manufactured components', fontsize=12)
        else:
            plt.xlabel('Manufactured components', fontsize=12)

    plt.ylabel("Unitary cost(€)", fontsize=12)
    plt.legend(cantidades, title='Mass production\n    rate(units)')

    plt.show()
