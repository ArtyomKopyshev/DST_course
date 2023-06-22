import pandas as pd

melb_df_fe = pd.read_csv('D:\IDE\SkillFactory\PY-11_Работа_с_данными\data\melb_data_fe.csv')
print(melb_df_fe.head())
print(melb_df_fe.info())
melb_df_fe['Date'] = pd.to_datetime(melb_df_fe['Date'], dayfirst=False)
print(melb_df_fe.head())
qart = melb_df_fe['Date'].dt.quarter
print(qart.value_counts())
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий
for col in melb_df_fe.columns: # цикл по именам столбцов
    if melb_df_fe[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        melb_df_fe[col] = melb_df_fe[col].astype('category') # преобразуем тип столбца
print(melb_df_fe.info())
print(melb_df_fe.sort_values(by='AreaRatio', ascending=False, ignore_index=True).loc[1558, ['BuildingArea']])
mask1 = melb_df_fe['Rooms'] > 2
mask2 = melb_df_fe['Type'] == 'townhouse'
print(round(melb_df_fe[mask1 & mask2].sort_values(
    by=['Rooms', 'MeanRoomsSquare'],
    ascending=[True, False],
    ignore_index=True
).loc[18, ['Price']][0]))
print(melb_df_fe.groupby('Rooms')['Price'].mean().sort_values(ascending=False))
print(melb_df_fe.groupby('Regionname')['Lattitude'].std().sort_values(ascending=True))
mask1 = melb_df_fe['Date'] >= pd.to_datetime('2017-05-01')
mask2 = melb_df_fe['Date'] <= pd.to_datetime('2017-09-01')
grouping_melb = melb_df_fe[mask1 & mask2].copy()
print(grouping_melb.groupby('SellerG')['Price'].sum().sort_values(ascending=False))