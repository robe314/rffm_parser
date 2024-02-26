from variables import url_seguidos
from text_dict import text
from infantiles import get_infantiles

def text_infantiles():
    myinfantiles=get_infantiles(url_seguidos)
    texto=text(myinfantiles)
    return texto