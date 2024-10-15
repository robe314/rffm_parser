from variables import url_calendario
from dict2text import dict2text
from dict_calendario import dict_calendario

mycalendario=dict_calendario(url_calendario)

texto=dict2text(mycalendario)

print (texto)