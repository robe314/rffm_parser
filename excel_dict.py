import pandas as pd

def excel(dict):
    df = pd.DataFrame.from_dict(dict)
    df.to_excel('borrar_excel.xlsx',index=False)