from geopy.geocoders import  Nominatim
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import requests

#Scrapper get the relevant data from the souce
preco = []
endereco = []
geocode = []

def Scrapper():
    options = Options()
    options.headless = True 

#url source 
    source = "https://www.zapimoveis.com.br/venda/imoveis/sp+santos"

#Initialize web driver 
    driver = webdriver.Firefox(options=options)
    driver.get(source)

#Initialize empty list

#Gets data from the site´s source
    for a in range(1,25):
        preco_source = driver.find_element_by_xpath("/html/body/main/section/div[2]/div[2]/section/div/div[{}]/div/div[2]/div[1]/p/strong".format(str(a)))
        endereco_source = driver.find_element_by_xpath("/html/body/main/section/div[2]/div[2]/section/div/div[{}]/div/div[2]/div[3]/p".format(str(a)))
        preco.append(preco_source.text)
        endereco.append(endereco_source.text)
# def geocode_generator():
    geolocator = Nominatim(user_agent="Preco_moradia")
    for i in range(len(endereco)):
        geocode.append(geolocator.geocode(endereco[i]))
    driver.close()
    return preco,endereco,geocode

