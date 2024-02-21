from text_dict import text
from resultados import get_resultados

myurl = "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145567"

def text_resultados():
    myresultados=get_resultados(myurl)
    texto=text(myresultados)
    return texto