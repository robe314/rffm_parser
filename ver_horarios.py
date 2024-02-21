from print_dict import print_dict
from horarios import get_horarios

myurl = "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145567"

myhorarios=get_horarios(myurl)
print_dict(myhorarios)