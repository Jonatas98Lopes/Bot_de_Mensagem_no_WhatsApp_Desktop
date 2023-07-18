import pyautogui as pg
import webbrowser
from actions import *
from interfaces_graficas.mensagem import Mensagem
from interfaces_graficas.quantidade_numeros import QuantidadeNumeros
from interfaces_graficas.aviso import Aviso
from interfaces_graficas.numero import Numero

mensagem_padrao = Mensagem()
mensagem = mensagem_padrao.values["mensagem"].strip()

while True:
    definir_quantidade_numeros = QuantidadeNumeros()
    qtd_numeros = definir_quantidade_numeros.values["quantidade_numeros"].strip()
    if qtd_numeros.isdigit() and qtd_numeros != '0':
        qtd_numeros = int(qtd_numeros)
        break
    
    Aviso('Informe um valor numérico maior que 0.')


numeros = []
for i in range(qtd_numeros):
    while True:
        numero_info = Numero(i + 1)
        numero = numero_info.values["numero"].strip()
        numero = filtrar_numero_telefone(numero)
        if numero.isdigit():
            numeros.append(numero)
            break

        Aviso('Informe um número de telefone no formato esperado.')


for posicao, numero in enumerate (numeros):
  
    webbrowser.open(f'https://api.whatsapp.com/send?phone={numero}')
    pausar()

    # Depende da resolução da sua tela.
    pg.click(673,352, duration=1.5)
    pausar()
    for i in range(2):
        pg.press("tab")
        pausar()
    pg.press("enter")
    pausar()
  
    if posicao == 0:    
        for i in range(11):
            pg.press("tab")
            sleep(0.5)

 
    digitar_caracteres_especiais(mensagem_padrao.values["mensagem"])    
    pausar()
    pg.press("enter")
 
    repousar()
    pg.hotkey('alt', 'tab')
    pausar()
    pg.hotkey('ctrl', 'w')
    pausar()

pg.hotkey('alt', 'f4')

Aviso('O programa foi encerrado com sucesso!')       

        