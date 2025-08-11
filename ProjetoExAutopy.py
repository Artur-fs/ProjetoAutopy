import pyautogui
import time
import pandas

# etapa 1 - Abrir o google chrome e o site
# etapa 2 - Logar no site
# etapa 3 - Importar base de dados
# etapa 4 - cadastrar produto

#etapa 1
pyautogui.PAUSE = 1
pyautogui.press ('win')
pyautogui.write ('Chrome')
pyautogui.press ('enter')
pyautogui.doubleClick (x=426, y=30)
time.sleep(2)
pyautogui.click (x=129, y=666)
pyautogui.doubleClick (x=713, y=28)
pyautogui.write ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press ('enter')

time.sleep(3)

#etapa 2
pyautogui.click (x=743, y=360)
pyautogui.write ('emailtest@gmail.com')
pyautogui.press ('tab')
pyautogui.write ('senhateste')
pyautogui.press ('enter')

#etapa 3
tabela = pandas.read_csv ('produtos.csv')

#etapa 4
for linha in tabela.index:
    pyautogui.click (x=715, y=254)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write (codigo)
    pyautogui.press ('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write (marca)
    pyautogui.press ('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write (tipo)
    pyautogui.press ('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write (str(categoria))
    pyautogui.press ('tab')

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write (str(preco_unitario))
    pyautogui.press ('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write (str(custo))
    pyautogui.press ('tab')

    obs = tabela.loc[linha, 'obs']
    
    if str(obs) != 'nan':
        pyautogui.write (str(obs))                
    
    pyautogui.press ('tab')    
    pyautogui.press ('enter')
    pyautogui.scroll (10000)