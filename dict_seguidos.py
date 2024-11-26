from web_parser import get_dict

def dict_seguidos(webs):
    lista = []
    for url in webs:
        mydict=get_dict(url)
        jornada = mydict['props']['pageProps']['results']['partidos']
        
        for partido in jornada:
            equipo_local = partido['Nombre_equipo_local']
            equipo_visitante = partido['Nombre_equipo_visitante']
            fecha = partido['fecha']
            hora = partido['hora']
            goles_casa = partido['Goles_casa']
            goles_visitante = partido['Goles_visitante']
            if "ADEPO PALOMERAS" in equipo_local or "ADEPO PALOMERAS" in equipo_visitante:
                lista.append({"Fecha" : fecha, "Hora" : hora, "Local" : equipo_local, "L" :goles_casa, "V" :goles_visitante, "Visitante" : equipo_visitante})
    return lista