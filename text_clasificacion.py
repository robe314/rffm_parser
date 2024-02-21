from text_dict import text
from clasificacion import get_clasificacion

myurl = "https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145567"

def text_clasificacion():
    myclasif=get_clasificacion(myurl)
    texto=text(myclasif)
    return texto