from web_parser import get_dict

def dict_infantiles(webs):
    lista = []
    for url in webs:
        mydict=get_dict(url)
        currentround = int(mydict['props']['pageProps']['currentRound'])-1
        jornada = mydict['props']['pageProps']['calendar']['rounds'][currentround]["equipos"]
        
        for partido in jornada:
            equipo_local = partido['equipo_local']
            equipo_visitante = partido['equipo_visitante']
            fecha = partido['fecha']
            hora = partido['hora']
            goles_casa = partido['goles_casa']
            goles_visitante = partido['goles_visitante']
            if "ADEPO PALOMERAS" in equipo_local or "ADEPO PALOMERAS" in equipo_visitante:
                lista.append({"Fecha" : fecha, "Hora" : hora, "Local" : equipo_local, "L" :goles_casa, "V" :goles_visitante, "Visitante" : equipo_visitante})
    return lista