from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import telebot
import time
import pyautogui
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()
    

TOKEN = os.getenv("token")
CHAT_ID = os.getenv("chat_id")

print(TOKEN,CHAT_ID)


bot = telebot.TeleBot(TOKEN)



url_origim_global = None
url_destino_global = None

@bot.message_handler(commands=['help', 'start'])
def start(message):
    bot.reply_to(message, "-Olá, sou seu assistente que vai lhe auxiliar a encontrar os melhores fretes para voce-\n")
    bot.reply_to(message, "De é a origem do local que vc deseja começar buscando seus fretes:\n")
    bot.reply_to(message, '''
            Clique no local de ORIGEM desejado:
            -----------------------------------
            SÃO PAULO: /Origem_Sp
            MINAS GERAIS: /Mg
            PARANÁ: /Pr
            SANTA CATARINA: /Sc
            BAHIA: /Ba
            ACRE: /Ac   
            ALAGOAS: /Al  
            AMAPÁ: /Ap
            AMAZONAS: /Am
            CEARÁ: /Ce
            DISTRITO FEDERAL: /Df
            ESPIRITO SANTO: /Es
            GOIÁS: /Go
            MARANHÃO: /Ma
            MATO GROSSO: /Mt
            MATO GROSSO DO SUL: /Ms
            PARÁ: /Pa
            PARAÍBA: /Pb
            RIO DE JANEIRO: /Rj
            RIO GRANDE DO NORTE: /Rn
            RIO GRANDE DO SUL: /Rs
            RONDÔNIA: /Ro
            RORAIMA: /Rr
            SERGIPE: /Se
            TOCANTINS: /To
    ''')

@bot.message_handler(commands=['Origem_Sp'])
def def_origin_url(message):
    global url_origim_global
    url_origim_global = message.text
    url_origim_global = str(url_origim_global)
    url_origim_global = url_origim_global[-2:].lower()
    
    bot.reply_to(message, '''
            Clique no local de DESTINO desejado:
            -----------------------------------
            SÃO PAULO: /Destino_Sp
            MINAS GERAIS: /Mg
            PARANÁ: /Destino_Pr
            SANTA CATARINA: /Sc
            BAHIA: /Ba
            ACRE: /Ac   
            ALAGOAS: /Al  
            AMAPÁ: /Ap
            AMAZONAS: /Am
            CEARÁ: /Ce
            DISTRITO FEDERAL: /Df
            ESPIRITO SANTO: /Es
            GOIÁS: /Go
            MARANHÃO: /Ma
            MATO GROSSO: /Mt
            MATO GROSSO DO SUL: /Ms
            PARÁ: /Pa
            PARAÍBA: /Pb
            RIO DE JANEIRO: /Rj
            RIO GRANDE DO NORTE: /Rn
            RIO GRANDE DO SUL: /Rs
            RONDÔNIA: /Ro
            RORAIMA: /Rr
            SERGIPE: /Se
            TOCANTINS: /To
    ''')

@bot.message_handler(commands=['Destino_Pr'])
def def_destino_url(message):
    global url_destino_global
    url_destino_global = message.text
    url_destino_global = str(url_destino_global)
    url_destino_global = url_destino_global[-2:].lower()
    bot.reply_to(message, "Começando busca...")


@bot.message_handler(commands=['começar'])
def buscar_imprimir_carga(message):
    print(f"Origem: {url_origim_global}, Destino: {url_destino_global}")

    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    URL = (f"https://www.fretebras.com.br/fretes/carga-de-{url_origim_global}/carga-para-{url_destino_global}")
    driver.get(URL)
    ultimo_cod_link = [None]


    while True:
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


            def search_xpaths(xpaths):
                for xpath in xpaths:
                    try:
                        informacao = driver.find_element(By.XPATH, xpath).text
                        return informacao
                    except NoSuchElementException:
                        pass


            #COLETA INFORMAÇÕES DO PRODUTO
            xpaths = [
                "/html/body/div[3]/div/div[1]/div/div[3]/div[2]/span[1]",
                "/html/body/div[3]/div/div[1]/div/div[4]/div[2]/span[1]",
                '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/span[1]',
                '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/span[1]',
                '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/span[1]', ]

            produto = search_xpaths(xpaths)

            #COLETA INFORMAÇÕES DO VEICULO

            xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/span/a'
                    '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[1]/span/a',
                    '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[1]/span/a',
                    '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[1]/span/a',
                    '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[1]/span/a'
                    ]
            veiculo = search_xpaths(xpaths)

            # COLETA INFORMAÇÕES DA CARROCERIA
            xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/span/a',
                    '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[2]/span/a',
                    '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[2]/span/a',
                    '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[2]/span/a',
                    '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[2]/span/a'
                    ]
            carroceria = search_xpaths(xpaths)

            # COLETA INFORMAÇÕES DO TIPO DA CARGA
            xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[5]/span',
                    '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[5]/span',
                    '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[5]/span',
                    '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[5]/span',
                    '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[5]/span'
                    ]
            tipo_carga = search_xpaths(xpaths)

            # COLETA INFORMAÇÕES DO RASTREIO
            xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[6]/span',
                    '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[6]/span',
                    '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[6]/span',
                    '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[6]/span',
                    '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[6]/span'
                    ]
            search_xpaths(xpaths)

            #INFORMAÇÕES SOBRE O AGENCIAMENTO
            xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[7]/span',
                    '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[7]/span',
                    '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[7]/span',
                    '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[7]/span',
                    '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[7]/span',
                    ]
            search_xpaths(xpaths)

            #ORIGEM E DESTINO
            
            origem_city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[1]/span/a[1]').text
            origem_estado = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[1]/span/a[2]').text
            origem = f'{origem_city} - {origem_estado}'
            origem = ('').join(origem)
            
            destino_city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[3]/span/a[1]').text
            destino_estado = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[3]/span/a[2]').text
            destino = f'{destino_city} - {destino_estado}'
            destino = ('').join(destino)

            
            bot.send_message(CHAT_ID, text=f'Link: {ultimo_link}\n Produto: {produto}\n Veiculo: {veiculo}\n Origem: {origem} \n Destino: {destino}\n Carroceria: {carroceria}\n Tipo carga: {tipo_carga}')

            driver.back()

        else:
            time.sleep(0.5)
            driver.refresh()
            
bot.infinity_polling()