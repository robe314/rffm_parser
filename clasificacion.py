from web_parser import get_dict

def get_clasificacion(url):
    mydict = get_dict(url)
    clasif=mydict['props']['pageProps']['standings']['clasificacion']
    myclasif=[]
    for i in clasif:
        myclasif.append({"Posicion":i["posicion"],"Nombre":i["nombre"],"Puntos":i["puntos"],"Jugados":i["jugados"],"Ganados":i["ganados"],"Empatados":i["empatados"],"Perdidos":i["perdidos"],"Goles_a_favor":i["goles_a_favor"],"Goles_en_contra":i["goles_en_contra"]})
    return myclasif