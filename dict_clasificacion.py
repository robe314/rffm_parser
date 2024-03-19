from web_parser import get_dict

def dict_clasificacion(url):
    mydict = get_dict(url)
    clasif=mydict['props']['pageProps']['standings']['clasificacion']
    myclasif=[]
    for i in clasif:
        myclasif.append({"Posicion":int(i["posicion"]),"Nombre":i["nombre"],"Puntos":int(i["puntos"]),"Jugados":int(i["jugados"]),"Ganados":int(i["ganados"]),"Empatados":int(i["empatados"]),"Perdidos":int(i["perdidos"]),"Goles_a_favor":int(i["goles_a_favor"]),"Goles_en_contra":int(i["goles_en_contra"])})
    return myclasif