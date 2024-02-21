from print_dict import print_dict
from resultados import get_resultados

myurl = "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145567"

myresultados=get_resultados(myurl)
print_dict(myresultados)