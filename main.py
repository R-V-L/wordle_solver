from bs4 import BeautifulSoup as bs
import requests
from unicodedata import normalize

# https://wordle.wekele.com/?

response = requests.get('https://raw.githubusercontent.com/mazyvan/most-common-spanish-words/master/most-common-spanish-words-v4.txt')
data = response.text.split('\n')
trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
nuevo_diccionario = []
tamano_palabra = 5

for palabra in data:
  if len(palabra) == tamano_palabra:
    palabra_normalizada = normalize('NFKC', normalize('NFKD', palabra).translate(trans_tab))
    if palabra_normalizada not in nuevo_diccionario:
      nuevo_diccionario.append(palabra_normalizada)

print(nuevo_diccionario)
#data.index(palabra)