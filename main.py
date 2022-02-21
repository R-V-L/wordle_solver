import requests
from unicodedata import normalize

# https://wordle.wekele.com/?

response = requests.get("https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/master/0_palabras_todas.txt")
data = response.text.split("\n")
trans_tab = dict.fromkeys(map(ord, u"\u0301\u0308"), None)
lista_palabras = []
tamano_palabra = 5

for palabra in data:
    if len(palabra) == tamano_palabra:
        palabra_normalizada = normalize("NFKC", normalize("NFKD", palabra).translate(trans_tab))
        if palabra_normalizada not in lista_palabras:
            lista_palabras.append(palabra_normalizada.lower())

no_contiene = {2: ['c', 'a'], 4: ['c']}
no_contiene_no_pos = ['f', 'e', 'i', 'z', 'd']
contiene = {3: "l", 5: 'a', 1: 'c'}
contiene_no_pos = ['c']

def no_contiene_func(lista_palabras: list, no_contiene_dict: dict, no_contiene_no_pos_list: list):
    if no_contiene_dict:
        lista_palabras_nuevo = []
        for palabra in lista_palabras:  
            if all(palabra[k-1] != i for k, v in no_contiene_dict.items() for i in v):
                if not any(letra in palabra for letra in no_contiene_no_pos_list):
                    lista_palabras_nuevo.append(palabra)
        return lista_palabras_nuevo
    else:
        return lista_palabras

def contiene_func(lista_palabras: list, contiene_list: dict, contiene_no_pos_list: list):
    if contiene_list:
        lista_palabras_nuevo = []
        for palabra in lista_palabras:
            if all((contiene_list[x] in palabra[x - 1] for x in contiene_list)) and (x in palabra for x in contiene_no_pos_list):
                lista_palabras_nuevo.append(palabra)
        return lista_palabras_nuevo
    else:
        return lista_palabras

lista_palabras = no_contiene_func(lista_palabras, no_contiene, no_contiene_no_pos)
lista_palabras = contiene_func(lista_palabras, contiene, contiene_no_pos)
print(len(lista_palabras))
print(lista_palabras)