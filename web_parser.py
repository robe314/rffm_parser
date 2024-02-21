import urllib.request, json
from bs4 import BeautifulSoup

def get_dict(url):
    temp=urllib.request.urlopen(url)
    html=temp.read()
    soup = BeautifulSoup(html,features="html.parser")
    datos=soup.body.script.contents[0]
    mydict = json.loads(datos)
    return mydict