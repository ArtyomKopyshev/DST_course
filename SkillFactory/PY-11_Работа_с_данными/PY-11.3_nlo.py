import pandas as pd

nlo_data = pd.read_csv('D:\IDE\SkillFactory\PY-11_Работа_с_данными\data\example.csv', sep=',')
print(nlo_data.head)
nlo_data['Time'] = pd.to_datetime(nlo_data['Time'], dayfirst=False)
nlo_data['Year'] = nlo_data['Time'].dt.year
print(nlo_data['Year'].mode()[0])
nlo_data_nevada = nlo_data[nlo_data['State'] == 'NV'].copy()
nlo_data_nevada['Date'] = nlo_data_nevada['Time'].dt.date
nlo_data_nevada['Diff'] = nlo_data_nevada['Date'].diff()
print(nlo_data_nevada.head)
#nlo_data_nevada['Diff'] = nlo_data_nevada['Diff']
print(nlo_data_nevada['Diff'].mean())