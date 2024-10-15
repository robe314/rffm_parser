from web_parser import get_dict
from variables import myequipo

def dict_calendario(url):
    lista = []
    mydict=get_dict(url)
    jornada = mydict['props']['pageProps']['calendar']['rounds']
    
    for a in jornada:
        for b in a['equipos']:
            equipo_local = b['equipo_local']
            equipo_visitante = b['equipo_visitante']
            fecha = b['fecha']
            hora = b['hora']
            goles_casa = b['goles_casa']
            goles_visitante = b['goles_visitante']
            if equipo_local == myequipo or equipo_visitante == myequipo:
                lista.append({"Fecha" : fecha, "Hora" : hora, "Local" : equipo_local, "Visitante" : equipo_visitante , "L" : goles_casa, "V" : goles_visitante})
    return lista