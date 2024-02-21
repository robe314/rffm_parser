from web_parser import get_dict

def get_resultados(url):
    mydict=get_dict(url)
    currentround = int(mydict['props']['pageProps']['currentRound'])-1
    jornada = mydict['props']['pageProps']['calendar']['rounds'][currentround]['equipos']
    myjornada=[]
    for i in jornada:
        myjornada.append({"Local":i["equipo_local"],"L":i["goles_casa"],"V":i["goles_visitante"],"Visitante":i["equipo_visitante"],"Fecha":i["fecha"],"Hora":i["hora"]})
    return myjornada