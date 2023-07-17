import PySimpleGUI as sg

class Mensagem:
	def __init__(self):
		sg.theme('LightGray')
		layout = [
			[sg.Text('Escreva a mensagem que deseja enviar para os contatos:',font='_ 14')],
			[sg.Multiline(size=(62,5), key='mensagem', font='_ 12')],
			[sg.Button('Enviar',size=(50,50))]]

		janela = sg.Window('Digite a mensagem que quer enviar:', font='_ 14', size=(550,170)).layout(layout)
	
		self.button, self.values = janela.Read()

		janela.close()

