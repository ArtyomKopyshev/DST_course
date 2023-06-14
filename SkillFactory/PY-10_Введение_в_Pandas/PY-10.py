import pandas as pd

melb_data = pd.read_csv('data/melb_data.csv', sep=',')
print(melb_data.loc[15, 'Price'])