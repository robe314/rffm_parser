from variables import url_resultados
from dict2text import dict2text
from dict_resultados import dict_resultados

myresultados=dict_resultados(url_resultados)
texto=dict2text(myresultados)

print (texto)