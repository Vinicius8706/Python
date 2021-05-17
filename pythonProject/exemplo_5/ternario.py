"""Operador ternário em Python"""

logged_user = False

msg = 'Usuario logado.' if logged_user == True else 'Usuario precisa logar.'

print(msg)
idade  = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Voce precisa digitar apenas numeros')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

    print(msg)