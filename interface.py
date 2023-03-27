import PySimpleGUI as sg

# Layout
sg.theme('reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha  '), sg.Input(key='senha')],
    [sg.Checkbox('salvar login')],
    [sg.Button('Entrar'), sg.Button('Sair')]
]
# Janela
janela = sg.Window('Tela de login', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
janela.close()
# Ler os eventos
if evento == 'Entrar':
    if valores['usuario'] == 'gerge' and valores['senha'] == '01100111':
        print('gerge')