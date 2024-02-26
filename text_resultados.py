from variables import url_calendario
from text_dict import text
from resultados import get_resultados

def text_resultados():
    myresultados=get_resultados(url_calendario)
    texto=text(myresultados)
    return texto