from variables import url_seguidos
from dict2text import dict2text
from dict_seguidos import dict_seguidos

myinfantiles=dict_seguidos(url_seguidos)
texto=dict2text(myinfantiles)

print (texto)