from variables import url_clasificacion
from dict2text import dict2text
from dict_clasificacion import dict_clasificacion

myclasif=dict_clasificacion(url_clasificacion)
texto=dict2text(myclasif)

print (texto)