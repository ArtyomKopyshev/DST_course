import pandas as pd

dates_df = pd.read_csv('D:\IDE\SkillFactory\PY-11_Работа_с_данными\data\dates.csv')
ratings1_df = pd.read_csv('D:\IDE\SkillFactory\PY-11_Работа_с_данными\data\cratings1.csv')
ratings2_df = pd.read_csv('D:\IDE\SkillFactory\PY-11_Работа_с_данными\data\cratings2.csv')
movies_df = pd.read_csv('D:\IDE\SkillFactory\PY-11_Работа_с_данными\data\movies.csv')
ratings = pd.concat(
    [ratings1_df, ratings2_df],
    ignore_index = True
)
ratings = ratings.drop_duplicates(ignore_index=True)
ratings_dates = pd.concat([ratings, dates_df], axis=1)
