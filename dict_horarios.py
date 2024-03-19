from web_parser import get_dict

def dict_horarios(url):
    lista = []
    mydict=get_dict(url)
    currentround = int(mydict['props']['pageProps']['currentRound'])-1
    jornada = mydict['props']['pageProps']['calendar']['rounds']
    for a in range(currentround,len(jornada)):
        for b in range(0,len(jornada[a]['equipos'])):
            equipo_local = jornada[a]['equipos'][b]['equipo_local']
            equipo_visitante = jornada[a]['equipos'][b]['equipo_visitante']
            fecha = jornada[a]['equipos'][b]['fecha']
            hora = jornada[a]['equipos'][b]['hora']
            if equipo_local == "ADEPO PALOMERAS 'A'" or equipo_visitante == "ADEPO PALOMERAS 'A'":
                lista.append({"Fecha" : fecha, "Hora" : hora, "Local" : equipo_local, "Visitante" : equipo_visitante})
    return lista