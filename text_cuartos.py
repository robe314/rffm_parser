from variables import url_cuartos
from text_dict import text
from cuartos import get_cuartos

def text_cuartos():
    mycuartos=get_cuartos(url_cuartos)
    texto=text(mycuartos)
    return texto