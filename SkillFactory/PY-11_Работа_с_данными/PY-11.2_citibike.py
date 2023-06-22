import pandas as pd

def get_time_of_day(date: pd.DatetimeIndex):
    if 0 <= date.hour <= 6:
        return 'night'
    if 6 < date.hour <= 12:
        return 'morning'
    if 12 < date.hour <= 18:
        return 'day'
    if 18 < date.hour <= 23:
        return 'evening'
    
citibike_df = pd.read_csv('D:\IDE\SkillFactory\PY-11_Работа_с_данными\data\citibike-tripdata.csv', sep=',')
print(citibike_df.info())
print(citibike_df['bikeid'].mode())
print(citibike_df['usertype'].value_counts(normalize=True))
print(citibike_df[citibike_df['gender'] == 1]['gender'].shape[0])
print(citibike_df[citibike_df['gender'] == 2]['gender'].shape[0])
print(citibike_df['start station id'].nunique())
print(citibike_df['end station id'].nunique())
print(citibike_df['birth year'].max())
print(citibike_df['start station name'].value_counts(normalize=True))
print(citibike_df['end station name'].mode())
citibike_df.drop(['start station id','end station id'],axis=1,inplace=True)
print(citibike_df.info())
citibike_df['age'] = citibike_df['birth year'].apply(lambda x: 2018 - x)
citibike_df.drop('birth year',axis=1,inplace=True)
print(citibike_df[citibike_df['age'] > 60].shape[0])
citibike_df['starttime'] = pd.to_datetime(citibike_df['starttime'], dayfirst=False)
citibike_df['stoptime'] = pd.to_datetime(citibike_df['stoptime'], dayfirst=False)
print(citibike_df.info())
citibike_df['trip duration'] = citibike_df['stoptime'] - citibike_df['starttime']
print(citibike_df.iloc[3])
citibike_df['weekend'] = citibike_df['starttime'].dt.day_of_week // 5
print(citibike_df[citibike_df['weekend'] == 1].shape[0])
citibike_df['time_of_day'] = citibike_df['starttime'].apply(get_time_of_day)
print(citibike_df.head())
print(round(citibike_df[citibike_df['time_of_day'] == 'day'].shape[0] / citibike_df[citibike_df['time_of_day'] == 'night'].shape[0]))