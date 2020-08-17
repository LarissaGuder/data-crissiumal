from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns


def plotPerColumnDistribution(nGraphShown, nGraphPerRow):
    df = pd.read_csv('../data/data.csv')  
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()
    plt.savefig('teste.png')

# plotPerColumnDistribution(10, 5)

### TODO: 
def valor_ano():
    df = pd.read_csv('../data/data.csv')
    plt.figure(figsize=(10,6))

    plt.title("Gastos por ano")
    groupedvalues=df.groupby('ANO').sum().reset_index()
    g = sns.barplot(x=df['ANO'], y=df['VL_LIQUIDADO'], data=groupedvalues, estimator=sum)
    ax=g
    ax.set_xlabel('ANO')
    for p in ax.patches:
                ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=11, color='gray', xytext=(0, 20),
                    textcoords='offset points')
    _ = g.set_ylim(0,50000000)
    

    plt.savefig('ano_vlliquidado_sum.pdf')
    
valor_ano()