from text_dict import text
from horario import get_horario

myurl = "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145567"

def text_horario():
    myhorario=get_horario(myurl)
    texto=text(myhorario)
    return texto