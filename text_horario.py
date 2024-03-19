from variables import url_calendario
from dict2text import dict2text
from dict_horarios import dict_horarios

def text_horario():
    myhorario=dict_horarios(url_calendario)
    texto=dict2text(myhorario)
    return texto