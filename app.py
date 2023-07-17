import pyautogui as pg
import webbrowser
from actions import *

""" QUAIS OS PASSOS MANUAIS PRECISO FAZER PARA ENVIAR UMA MENSAGEM PARA VÁRIAS PESSOAS.

REQUESITOS:

* TER O WHATSAPP DESKTOP INSTALADO NO SEU NAVEGADOR.

* TER A MINHA MENSAGEM PRONTA.

* TER UMA LISTA COM OS NÚMEROS DOS CONTATOS.
 """
# ALGORITMO:

#1 - OBTER A MENSAGEM A ENVIAR.
mensagem = pg.prompt(text='Informe a mensagem que deseja enviar.', title='Mensagem Requisitada:').strip()
#2 - OBTER OS NÚMEROS DOS CONTATOS.
while True:
    qtd_numeros = pg.prompt(text='Para quantos contatos você deseja enviar essa mensagem?', title='Quantidade de Contatos:').strip()
    if qtd_numeros.isdigit() and qtd_numeros != '0':
        qtd_numeros = int(qtd_numeros)
        break

    pg.alert(text='Informe um valor numérico maior que 0.', title='AVISO!', button='Ok?')

numeros = []
for i in range(qtd_numeros):
    while True:
        numero = pg.prompt(text=f'Informe o {i + 1}º número. Exemplo do formato: +55 11 99999-9999', title='Informe o número:').strip()
        numero = filtrar_numero_telefone(numero)
        if numero.isdigit():
            numeros.append(numero)
            break

        pg.alert(text='Informe um número de telefone no formato esperado.', title='Aviso!', button='Ok?')

# PARA CADA CONTATO, FAÇA O SEGUINTE:
for posicao, numero in enumerate (numeros):
    #3 	- ABRIR O NAVEGADOR.
    #4 	- ACESSAR  O SITE: https://api.whatsapp.com/send?phone=NUMERODOCONTATO
    webbrowser.open(f'https://api.whatsapp.com/send?phone={numero}')
    pausar()
    #5 	- CLICAR EM "ABRIR" - O WHATSAPP DESKTOP.
    botao_iniciar = pg.locateCenterOnScreen('./images/iniciarConversa.png')
    pausar()
    pg.click(botao_iniciar[0], botao_iniciar[1], duration=1.5)
    pausar()
    for i in range(2):
        pg.press("tab")
        pausar()
    pg.press("enter")
    pausar()
    #6 	- SELECIONAR A BARRA DE MENSAGEM.
    if posicao == 0:    
        for i in range(11):
            pg.press("tab")
            sleep(0.5)

    #7 	- ESCREVER A MENSAGEM PRONTA.
    digitar_caracteres_especiais(mensagem)    
    pausar()
    #8 	- CLICAR PARA ENVIAR A MENSAGEM.
    pg.press("enter")
    #9 	- PAUSAR OPERAÇÃO.
    repousar()
    pg.hotkey('alt', 'tab')
    pausar()
    pg.hotkey('ctrl', 'w')
    pausar()

        

        