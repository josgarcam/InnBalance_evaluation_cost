import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter

def labels_vs_cost(result, cantidades, query_conditions):

    df = pd.DataFrame(data=result).transpose().round(decimals=0)
    ax = df.plot(rot=20, kind='bar', color=['#AFCB1D', '#00000066', '#545454', '#86C05E', 'black'], width=0.8)
    print("++++++ ", result)

    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() * 1.005, p.get_height() * 1.005), rotation=45, size=10, fontweight='bold')

    plt.grid()
    # pd.DataFrame()

    # if query_conditions.get('origin') == 'B':
    #     if query_conditions.get('manuforiented') == False:
    #         plt.xlabel('Bought components', fontsize=12)
    #     else:
    #         plt.xlabel('Bought components', fontsize=12)
    # else:
    #     if query_conditions.get('manuforiented') == True:
    #         plt.xlabel('Manufactured components', fontsize=12)
    #     else:
    #         plt.xlabel('Manufactured components', fontsize=12)

    plt.ylabel("Unitary cost [€]", fontsize=12)
    plt.legend(cantidades, title='Mass production\n    rate(units)', loc='upper left')
    plt.ylim(0,2600)
    plt.grid(lw=0.1)
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))


    plt.show()
