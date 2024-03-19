from variables import url_seguidos
from dict2text import dict2text
from dict_infantiles import dict_infantiles

def text_infantiles():
    myinfantiles=dict_infantiles(url_seguidos)
    texto=dict2text(myinfantiles)
    return texto