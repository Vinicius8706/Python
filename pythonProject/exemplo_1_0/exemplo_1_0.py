"""
Condições IF, ELIF e ELSE - Aula 4
"""
# if False:
#   print('Verdadeiro')
# elif False:
#   print('Agora é verdadeiro')
# elif False:
#   print('Mais uma verdadeira')
# else:
#   print('Nao é verdadeiro')
  
# nome = input('Qual o seu nome? ')
# idade = input('Qual a sua idade? ')

# idade = int(idade)
# idade_menor = 20
# idade_maior = 30

# if( idade >= idade_limite ):
#   print(f'{nome} pode pegar o empréstimo')
  
# else:
#   print(f'{nome} não pode pegar o empréstimo')

a = 2
b = 3

if b >a:
  print('B é maior do que A.')
  
else:
  print('A é maior do que B')

nome = 'Vinicius'

if 'u' in nome:
  print('Existe a letra U no seu nome.')
  
else:
  print('Não existe.')
  
usuario = input('Nome de usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
  print('Voce está logado no sistema.')
else:
  print("Usuario ou senha invalidos")