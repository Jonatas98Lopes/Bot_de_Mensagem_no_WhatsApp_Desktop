import PySimpleGUI as sg

class Numero:
	def __init__(self, numero):
		sg.theme('LightGray')
		layout = [
			[sg.Text(f'Informe o {numero}º número. Exemplo do formato: +55 11 99999-9999',font='_ 14')], 
			[sg.Input(size=(62,10), key='numero', font='_ 12')],
			[sg.Button('Enviar',size=(50,1))]]

		janela = sg.Window('Informe o número:', font='_ 14', size=(575,100)).layout(layout)
	
		self.button, self.values = janela.Read()

		janela.close()
