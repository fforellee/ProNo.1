import os
import requests
from bs4 import BeautifulSoup

#search_length = int(input("digite o tamanho da pesquisa "))

#a = "terrenos na regiao de santos"
source = "https://www.zapimoveis.com.br/venda/imoveis/sp+santos"
# donwloading source pages
r = requests.get(source[0:len(source)])
htmlsource = BeautifulSoup(r.text, 'lxml')
print(htmlsource.prettify())
match = htmlsource.html
print(match)

































































































