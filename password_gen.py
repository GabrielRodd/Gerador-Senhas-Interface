# Importar bibliotecas
import random  # Bibli. random gera valores aleatorios
import string  # Bibli. string para gerar strings
import PySimpleGUI as sg  # Bibli. de interface gráfica


class PassGen:
    def __init__(self):
        # Layout
        sg.theme('BluePurple')
        layout1 = [
            [sg.Text('Site/Software', size=(11, 1), colors=('black')),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(11, 1), colors=('black')),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Primeiro Caracter', size=(11, 1), colors=('black')),
             sg.Input(key='first', size=(20, 1))],
            [sg.Text('Quantidade de caracteres', size=(20, 1), colors=('black')),
             sg.Combo(values=list(range(31)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
    
        # Declarar janela
        self.janela = sg.Window('Password Generator', layout1)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(f'Senha gerada pelo sistema:\n{nova_senha}')

    def gerar_senha(self, valores):
        letter_options = string.ascii_letters
        digit_options = string.digits
        punt_options = string.punctuation
        options = letter_options+digit_options+punt_options
        chars = random.choices(options, k=int(valores['total_chars'] - 1))
        primeiro_carac = valores['first']
        new_pass = primeiro_carac + ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {
                          valores['usuario']}, nova senha {nova_senha} ")

        print('Arquivo Salvo')


gen = PassGen()
gen.Iniciar()
