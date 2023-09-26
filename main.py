# Imports de bibliotecas
import pandas as pd
import pyautogui
import time

# Leitura da tabela com pandas, e adição da mesma em uma variavel (tabela)
tabela = pd.read_csv('produtos.csv')

# Tempo de espera entre os comandos pyautogui abaixo
pyautogui.PAUSE = 0.7

# Abrir o sistema dentro do navegador especificado
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Tempo para esperar o site carregar
time.sleep(5)

# Fazer login 
pyautogui.click(x=2241, y=233)
pyautogui.write('exemplo@email.com')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')

# Laço de repetição para percorrer as linhas da tabela a adicionar os produtos em cada campo do sistema
for linha in tabela.index:
    pyautogui.click(x=2122, y=116)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)