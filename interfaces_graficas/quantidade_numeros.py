import PySimpleGUI as sg

class QuantidadeNumeros:
	def __init__(self):
		sg.theme('LightGray')
		layout = [
			[sg.Text('Para quantos deseja enviar a mensagem?',font='_ 14')],
			[sg.Input(size=(40,5), key='quantidade_numeros', font='_ 12')],
			[sg.Button('Enviar',size=(20,2))]]

		janela = sg.Window('Quantidade de contatos:', font='_ 8', size=(420,120)).layout(layout)
	
		self.button, self.values = janela.Read()

		janela.close()
