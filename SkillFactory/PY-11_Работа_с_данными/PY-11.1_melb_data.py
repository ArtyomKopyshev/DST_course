import pandas as pd

melb_data = pd.read_csv('D:\IDE\SkillFactory\PY-11_Работа_с_данными\data\melb_data_ps.csv', sep=',')
melb_df = melb_data.copy()
#print(melb_df.head())
melb_df.drop(['index','Coordinates'],axis=1,inplace=True)
#print(melb_df.head())
total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
melb_df['MeanRoomsSquare'] = melb_df['BuildingArea'] / total_rooms
#print(melb_df['MeanRoomsSquare'])
diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
#print(melb_df['AreaRatio'])
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
#print(melb_df['AgeBuilding'])
melb_df = melb_df.drop('YearBuilt', axis=1)
melb_df['day_of_week'] = melb_df['Date'].dt.day_of_week
weekend_day = melb_df[melb_df['day_of_week'] > 4].shape[0]
#print(round(melb_df[melb_df['day_of_week'] > 4]['Price'].mean()))
#print(melb_df['SellerG'].nunique())
popular_org = melb_df['SellerG'].value_counts().nlargest(49).index
melb_df['Saller_group'] = melb_df['SellerG'].apply(lambda x: x if x in popular_org else 'other')
nelson_min_price = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min()
#print(nelson_min_price)
other_min_price = melb_df[melb_df['Saller_group'] == 'other']['Price'].min()
#print(other_min_price)
result = nelson_min_price / other_min_price
#print(round(result, 1))
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий
for col in melb_df.columns: # цикл по именам столбцов
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        melb_df[col] = melb_df[col].astype('category') # преобразуем тип столбца
print(melb_df.info())
popular_sub = melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in popular_org else 'other')
melb_df['Suburb'] = melb_df['Suburb'].astype('category')
print(melb_df.info())