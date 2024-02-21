from tabulate import tabulate

def text(dict):
    texto=tabulate(dict,headers="keys")
    return texto