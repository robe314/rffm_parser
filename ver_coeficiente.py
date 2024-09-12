from variables import url_coeficiente
from variables import puesto
from dict2text import dict2text
from dict_coeficiente import dict_coeficiente

mycuartos=dict_coeficiente(url_coeficiente,puesto)
texto=dict2text(mycuartos)

print(texto)