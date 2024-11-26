# Echar un vistazo porque en el diccionario parece haber un campo: 'coeficiente': '0.00' - ACTUALIZACION: Ha desaparecido ese campo

import operator
from web_parser import get_dict

def dict_coeficiente(webs,puesto):
    lista = []
    grupo=1
    for url in webs:
        mydict=get_dict(url)
        equipo=mydict['props']['pageProps']['standings']['clasificacion'][puesto-1]
        nombre=equipo["nombre"]
        jugados=int(equipo["jugados"])
        puntos=int(equipo["puntos"])
        #coeficiente=float(equipo["coeficiente"])
        lista.append({"Grupo":grupo,"Nombre":nombre,"Jugados":jugados,"Puntos":puntos,"Coeficiente":puntos/jugados})
        grupo+=1
    lista.sort(key=operator.itemgetter('Coeficiente'), reverse=True)
    return lista