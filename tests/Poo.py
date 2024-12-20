from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pyautogui

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

URL = 'https://www.fretebras.com.br/fretes/carga-de-pr/carga-para-mg'
driver.get(URL)
ultimo_cod_link = [None]

class XPATHS():

    def get_xpaths():
        links = driver.find_elements(By.XPATH,  '//*[@id="__next"]/main/div/fuel-grid-container/fuel-grid-item[2]/main/fuel-grid-item/div/a[1]')
        href = [link.get_attribute('href') for link in links]
        cod_link = (href[0][-14:-1])

        if cod_link not in ultimo_cod_link:
            ultimo_link = href
            ultimo_cod_link.append(cod_link)
            #ENTRARA COMANDO PARA O BOT E PARA COLETAR DADOS DO SITE
            time.sleep(1)
            print(ultimo_link)
            pyautogui.click(x=871, y=381)
            time.sleep(1)  
        else:
            time.sleep(0.7)
            driver.refresh()

    def search_xpaths(xpaths):
        for xpath in xpaths:
            try:
                informacao = driver.find_element(By.XPATH, xpath).text
                return informacao
            except NoSuchElementException:
                pass


class Frete(XPATHS):
        
        def __init__(self, xpaths):
            self.xpaths = xpaths

        def get_produto(self):
            produto = XPATHS.search_xpaths(self.xpaths)
            return produto

        #COLETA INFORMAÇÕES DO VEICULO

        def get_produto(self):
            veiculo = XPATHS.search_xpaths(self.xpaths)
            return veiculo

        # COLETA INFORMAÇÕES DA CARROCERIA
        def get_carroceria(self):
            carroceria = XPATHS.search_xpaths(self.xpaths)
            return carroceria 

        # COLETA INFORMAÇÕES DO TIPO DA CARGA
        def get_tipo_carga(self):
            tipo_carga = XPATHS.search_xpaths(self.xpaths)
            return tipo_carga
        

        # COLETA INFORMAÇÕES DO RASTREIO
        def get_rastreio(self):
            rastreio = XPATHS.search_xpaths(self.xpaths)
            return rastreio
        
        def get_agenciamento(self):
        #INFORMAÇÕES SOBRE O AGENCIAMENTO
            agenciameto = XPATHS.search_xpaths(self.xpaths)
            return agenciameto

        #ORIGEM E DESTINO
        def get_origim(self):
            origem_city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[1]/span/a[1]').text
            origem_estado = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[1]/span/a[2]').text
            origem = f'{origem_city} - {origem_estado}'
            return origem
        
        def get_destino(self):
            destino_city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[3]/span/a[1]').text
            destino_estado = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[3]/span/a[2]').text
            destino = f'{destino_city} - {destino_estado}'
            return destino
        

        driver.back()

x = XPATHS
f = Frete

xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[7]/span',
                  ]
while True:
    x.get_xpaths()
    agenciamento = f.get_agenciamento(['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[7]/span',
                  ])
    print(agenciamento, xpaths)
    print (agenciamento)
