import pandas as pd
import dataframe_image as dfi

def png(dict):
    df = pd.DataFrame(dict)
    dfi.export(df.style.hide(axis='index'), 'borrar.png')