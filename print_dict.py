from tabulate import tabulate

def print_dict(dict):
    texto=tabulate(dict,headers="keys")
    print (texto)