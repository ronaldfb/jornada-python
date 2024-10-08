# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.5

# abri o navegador
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
# entra no link 
pyautogui.click(x=319, y=61)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login

# seleciona o campo de email
pyautogui.click(x=531, y=371)
# escreve o seu email
pyautogui.write("meuemail@gmail.com")
#passa para outro campo
pyautogui.press("tab")
pyautogui.write("$minhasenha$123321$")
pyautogui.click(x=762, y=553)
time.sleep(2)

# Passo 3: Importar a base de produtos pra cadastrar

import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto



# pegar da tabela o valor do campo que a gente quer preencher
for linha in tabela.index:

    # clicar no campo de código
    pyautogui.click(x=511, y=251)
    
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo)) # preencher o campo
    pyautogui.press("tab") # passar para o proximo campo

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # cadastra o produto (botao enviar)
    pyautogui.press("enter")

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

 # Passo 5: Repetir o processo de cadastro até o fim
