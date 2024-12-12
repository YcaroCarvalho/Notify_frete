from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=service, options=options)

URL = (f"https://www.fretebras.com.br/fretes/carga-de-pr/carga-para-sp")
driver.get(URL)
ultimo_cod_link = [None]