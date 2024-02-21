from text_dict import text
from infantiles import get_infantiles

mywebs = ["https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145567",
        "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145568",
        "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145570&grupo=17145602"]

def text_infantiles():
    myinfantiles=get_infantiles(mywebs)
    texto=text(myinfantiles)
    return texto