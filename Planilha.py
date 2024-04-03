from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

tabela = pd.read_excel("Dados.xlsx");
print(tabela)

for i, nome in enumerate(tabela["Nome"]):
    email = tabela.loc[i,"Email"]
    cpf = tabela.loc[i,"CPF"]
    profissao = tabela.loc[i,"Profissão"]

    navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSfYAsJPCHfgPTKMAAETERWG3jLwOyUxTdgEdIGWJbkzK8YqAw/viewform?usp=sf_link")

    time.sleep(3);
    navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(nome);

    navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(email);

    navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(str(cpf));

    navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(profissao);

    navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click();
