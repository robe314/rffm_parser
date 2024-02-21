from print_dict import print_dict
from cuartos import get_cuartos

mywebs=["https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145554",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145555",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145556",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145557",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145558",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145559",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145560",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145561",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145562",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145563",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145564",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145565",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145566",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145567",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145568",
"https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145569"]

mycuartos=get_cuartos(mywebs)
print_dict(mycuartos)