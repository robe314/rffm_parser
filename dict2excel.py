import pandas as pd

def dict2excel(dict):
    df = pd.DataFrame.from_dict(dict)
    df.to_excel('borrar_excel.xlsx',index=False)