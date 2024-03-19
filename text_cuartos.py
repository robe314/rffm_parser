from variables import url_cuartos
from dict2text import dict2text
from dict_cuartos import dict_cuartos

def text_cuartos():
    mycuartos=dict_cuartos(url_cuartos)
    texto=dict2text(mycuartos)
    return texto