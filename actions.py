import pyperclip, pyautogui
from time import sleep
from random import randint


def filtrar_numero_telefone(telefone):
	"""
	A função receber APENAS um parâmetro: uma string representando o número de telefone.

	Filtra os caracteres especiais do número e o devolve.
	
	A função remove os seguintes caracteres:
	- '+';
 	- '-';
	- Chama a função remover_espaços_textuais para remover espaços numa string. 
	 """
	numero = telefone
	if telefone.find('+') != -1:
		numero = numero.split('+')[1]
	if numero.find('-') != -1:
		numero = numero.split('-')[0] + numero.split('-')[1]
	numero = remover_espacos_textuais(numero)
	return numero


def remover_espacos_textuais(string):
	"""
	A função receber APENAS um parâmetro: uma string.

	Esta a função recebe uma string e remove seu caracteres de espaço, devolvendo uma nova string sem espaços.
	"""
	caracteres = list(string)
	for caractere in string:
		if caractere == ' ':
			caracteres.remove(caractere)
	return "".join(caracteres)


def digitar_caracteres_especiais(frase):
	"""
  Essa função nos permite digitar textos com caracteres especiais como: à, á, é, ç...
  
  Ela aceita um único parametro chamado 'frase' onde frase é uma string.
  """
	pyperclip.copy(frase)
	pyautogui.hotkey('ctrl', 'v')
	
def pausar():
	"""
  Faz o programa ficar parado de 2 até 5 segundos. O tempo em que o programa ficará pausado é definido aleatoriamente.
  
  Esta função não aceita parâmetros.
  """
	sleep(randint(2, 5))
	
def repousar():
	"""
  Faz o programa ficar parado de 8 até 10 segundos. O tempo em que o programa ficará pausado é definido aleatoriamente.
  
  Esta função não aceita parâmetros.
  """
	sleep(randint(8, 10))

