from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

# Definir o caminho para o ChromeDriver
driver_path = r'C:\webdrivers\chromedriver.exe'
service = Service(driver_path)

# Inicializar o WebDriver
try:
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.petz.com.br/nossas-lojas')
    
    # Verifica se a página foi carregada
    print("Título da Página:", driver.title)
    print("O site está acessível!")
except WebDriverException as e:
    print("Erro ao acessar o site:", e)
finally:
    # Fechar o navegador
    driver.quit()