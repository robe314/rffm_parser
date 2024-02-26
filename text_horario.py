from variables import url_calendario
from text_dict import text
from horarios import get_horarios

def text_horario():
    myhorario=get_horarios(url_calendario)
    texto=text(myhorario)
    return texto