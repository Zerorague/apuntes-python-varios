import re
from bs4 import BeautifulSoup
import requests
import unidecode


def obtener_datos_brutos(url, etiqueta, clas):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    html = soup.find_all(etiqueta, class_=clas)
    return html


def obtener_links(url, etiqueta):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    html = soup.find_all(etiqueta, href=True)
    return html


def lista_datos(html):
    lista_publicaciones = []
    count = 0
    for i in html:
        if count < 100:
            lista_publicaciones.append(i.text)
            count += 1
        else:
            break
    return lista_publicaciones


def links(html):
    lista_links = []
    count = 0
    for i in html:
        if count < 100:
            lista_links.append(i.get("href"))
            count += 1
        else:
            break
    return lista_links


def publicar(lista_trabajos, lista_links, separador):
    for i in lista_trabajos:
        i = str(i).lower()
        i = i.replace(" ", separador)
        i = i.replace("\n", "")
        i = unidecode.unidecode(i)
        print(i)
        for l in lista_links:
            if i in l:
                print(f"{l}\n-------------------------")
                break
            else:

                continue
        pass


# ---------------chile trabajos--------------
chile_trabajos_html = obtener_datos_brutos(
    "https://www.chiletrabajos.cl/encuentra-un-empleo?2=topografo&13=1033&fecha=&categoria=&8=&14=&inclusion=&f=2", "h2", "title")
chile_trabajos_links = obtener_links(
    "https://www.chiletrabajos.cl/encuentra-un-empleo?2=topografo&13=1033&fecha=&categoria=&8=&14=&inclusion=&f=2", "a")
lista_trabajos_chile_trabajos = lista_datos(chile_trabajos_html)
links_chile_trabajos = links(chile_trabajos_links)
publicar(lista_trabajos_chile_trabajos,
         links_chile_trabajos, "-")




exit = input()
