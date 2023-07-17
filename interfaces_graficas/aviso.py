import PySimpleGUI as sg

class Aviso:
	def __init__(self, mensagem):
		sg.theme('LightGray')
		layout = [
			[sg.Text(mensagem, font='_ 14')],
			[sg.Button('Ok?',size=(42,1))]]

		janela = sg.Window('Aviso!', font='_ 14', size=(500,100)).layout(layout)
		
		self.button, self.values = janela.Read()

		janela.close()