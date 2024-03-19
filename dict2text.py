import pandas as pd

def dict2text(dict):
    df = pd.DataFrame.from_dict(dict)
    return df.to_markdown(index=False,tablefmt="plain")