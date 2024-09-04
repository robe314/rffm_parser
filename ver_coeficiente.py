from variables import url_coeficiente
from dict2text import dict2text
from dict_coeficiente import dict_coeficiente

mycuartos=dict_coeficiente(url_coeficiente,4)
texto=dict2text(mycuartos)

print(texto)