import pandas as pd

def create_companyDF(income, expenses, years):
    df = pd.DataFrame([income, expenses], columns=['income','expenses'], index = years)
    return df
    
def get_profit(df, year):
    if year in df.index:
        return df.loc[year, [income]] - df.loc[year, [expenses]]
    else:
        return None
    
income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]
df = create_companyDF(income, expenses, years)
print(get_profit(df, 2018))