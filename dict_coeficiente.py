import operator
from web_parser import get_dict

def dict_coeficiente(webs,puesto):
    lista = []
    grupo=1
    for url in webs:
        mydict=get_dict(url)
        cuarto=mydict['props']['pageProps']['standings']['clasificacion'][puesto-1]
        nombre=cuarto["nombre"]
        jugados=int(cuarto["jugados"])
        puntos=int(cuarto["puntos"])
        lista.append({"Grupo":grupo,"Nombre":nombre,"Jugados":jugados,"Puntos":puntos,"Coeficiente":puntos/jugados})
        grupo+=1
    lista.sort(key=operator.itemgetter('Coeficiente'), reverse=True)
    return lista