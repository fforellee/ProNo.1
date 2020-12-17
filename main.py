from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import requests

#Scrapper get the relevant data from the souce
def Scrapper():
    options = Options()
    options.headless = True 
    #url source 
    source = "https://www.zapimoveis.com.br/venda/imoveis/sp+santos"
    #Initialize web driver 
    driver = webdriver.Firefox()
    driver.get(source)
    #Initialize empty list
    preco = []
    endereco = []
    #Gets data from the site´s source
    for i in range(1,20):
        preco_source = driver.find_element_by_xpath("/html/body/main/section/div[2]/div[2]/section/div/div[%s]/div/div[2]/div[1]/p/strong" %(str(i)))
        endereco_source = driver.find_element_by_xpath("/html/body/main/section/div[2]/div[2]/section/div/div[%s]/div/div[2]/div[3]/p"%(str(i)))
        preco.append(preco_source.text)
        endereco.append(endereco_source.text)
    driver.close()
    return preco,endereco


Scrapper()
