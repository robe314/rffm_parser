from print_dict import print_dict
from clasificacion import get_clasificacion

myurl = "https://www.rffm.es/competicion/clasificaciones?temporada=19&competicion=17145553&grupo=17145567"

myclasif=get_clasificacion(myurl)
print_dict(myclasif)