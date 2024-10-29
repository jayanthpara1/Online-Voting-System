import pandas as pd

def print_excel_data():
    df = pd.read_excel('userdata.xlsx')
    print(df)

print_excel_data()
