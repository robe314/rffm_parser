from variables import url_clasificacion
from text_dict import text
from clasificacion import get_clasificacion

def text_clasificacion():
    myclasif=get_clasificacion(url_clasificacion)
    texto=text(myclasif)
    return texto