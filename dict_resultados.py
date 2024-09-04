from web_parser import get_dict

def dict_resultados(url):
    mydict=get_dict(url)
    jornada = mydict['props']['pageProps']['calendario']['partidos']
    myjornada=[]
    for i in jornada:
        myjornada.append({"Local":i["Nombre_equipo_local"],"L":i["Goles_casa"],"V":i["Goles_visitante"],"Visitante":i["Nombre_equipo_visitante"],"Fecha":i["fecha"],"Hora":i["hora"]})
    return myjornada