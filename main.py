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

    #Gets data from the site´s source
    for i in range(1,10):
        preco_source = driver.find_element_by_xpath("/html/body/main/section/div[2]/div[2]/section/div/div[%s]/div/div[2]/div[1]/p/strong" %(str(i)))
        endereco_source = driver.find_element_by_xpath("/html/body/main/section/div[2]/div[2]/section/div/div[%s]/div/div[2]/div[3]/p"%(str(i)))
        preco = [None]*10
        endereco =[None]*10
        preco[i] = preco_source.text
        endereco[i] = endereco_source.text
        print(preco[i])
        print(endereco[i])

    driver.close()
    return preco,endereco
Scrapper()



