
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os
import time


def clear():
    
    if os.name == 'nt':
        _ = os.system('cls')

def pegar_lista_idiomas():
    teste = "Olá Mundo"
    driver = webdriver.Chrome()
    driver.get("https://www.reverso.net")

    time.sleep(6);
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-translation/div/app-translation-box/div[1]/div[1]/div[1]/app-language-switch/div/app-language-select[1]"))).click()

    time.sleep(3)
    lista_idiomas = put_lang_to_translate(driver, "/html/body/div[2]/app-language-select-options/div/ul", "Português")
    driver.find_element(By.XPATH, "/html/body/app-root/app-translation/div/app-translation-box/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/textarea").send_keys(teste)
    retorno = []


    for idioma in lista_idiomas:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-translation/div/app-translation-box/div[1]/div[1]/div[1]/app-language-switch/div/app-language-select[2]/div/div"))).click()
          #  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-translation/div/app-translation-box/div[1]/div[1]/div[1]/app-language-switch/div/app-language-select[2]"))).click()
            time.sleep(5)
            put_lang_to_translate(driver, "/html/body/div[3]/app-language-select-options/div", idioma)
            time.sleep(5)
            valor = driver.find_element(By.XPATH, "/html/body/app-root/app-translation/div/app-translation-box/div[1]/div[1]/div[2]/div[2]/div[1]")
            valor = valor.text
            res = valor.replace("\n", " ou: ");
            clear();
            if not valor:
                valor = driver.find_element(By.XPATH, "/html/body/app-root/app-translation/div/app-translation-box/div[1]/div[1]/div[2]/div[2]/div[1]/div/span")
            retorno.append(f"{teste} em {idioma} é: {res}")
            
      
    return retorno

def put_lang_to_translate(driver, element, lang):
    try:

        nav = driver.find_element(By.XPATH, element);
        link_items = nav.find_elements(By.CLASS_NAME, "lang-label")
       # link_items = nav.find_elements(By.TAG_NAME, "li")
       
        topics = [item.text for item in link_items[9:13]]

        
        for item in link_items:
         
            if item.text == lang:
               
                item.click()
                break

        return topics
    except TimeoutException as ex:
        print("Elemento não encontrado:", ex)


resultado = pegar_lista_idiomas();
clear();
for i, item in enumerate(resultado, 1):
    print(item)
    
