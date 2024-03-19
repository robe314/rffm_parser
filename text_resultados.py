from variables import url_calendario
from dict2text import dict2text
from dict_resultados import dict_resultados

def text_resultados():
    myresultados=dict_resultados(url_calendario)
    texto=dict2text(myresultados)
    return texto