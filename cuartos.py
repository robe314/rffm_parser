import operator
from web_parser import get_dict

def get_cuartos(webs):
    lista = []
    grupo=1
    for url in webs:
        mydict=get_dict(url)
        cuarto=mydict['props']['pageProps']['standings']['clasificacion'][3]
        nombre=cuarto["nombre"]
        jugados=cuarto["jugados"]
        puntos=cuarto["puntos"]
        lista.append({"Grupo":grupo,"Nombre":nombre,"Jugados":jugados,"Puntos":puntos,"Coeficiente":int(puntos)/int(jugados)})
        grupo+=1
    lista.sort(key=operator.itemgetter('Coeficiente'), reverse=True)
    return lista