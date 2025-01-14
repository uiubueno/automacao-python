import pyautogui

pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

# fazer login

pyautogui.click(x=-793, y=853)

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.press("enter")

import pandas
import time 

database = pandas.read_csv("produtos.csv")

print(database)

time.sleep(2)

for line in database.index: 
    pyautogui.press("tab")
    
    # codigo 
    codigo = database.loc[line, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = database.loc[line, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo 
    tipo = database.loc[line, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria 
    categoria = database.loc[line, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco 
    preco_unitario = database.loc[line, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo 
    custo = database.loc[line, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs 
    obs = str(database.loc[line, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    # cadastrar-produto
    pyautogui.press("enter")

    # scrollar a tela pra cima
    # pyautogui.scroll(10000)       
    
    pyautogui.press("home")

