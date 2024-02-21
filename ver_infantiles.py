from print_dict import print_dict
from infantiles import get_infantiles

mywebs = ["https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145567",
        "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145568",
        "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145570&grupo=17145602"]

myinfantiles=get_infantiles(mywebs)
print_dict(myinfantiles)