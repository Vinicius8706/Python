"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Vinicius'
print(nome, type(nome))
idade = 20 #int
altura = 1.95 #float
e_maior = idade > 18

peso = 79

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior: ', e_maior)
print(idade * altura)
imc = (peso) / (altura ** 2)
print('{} tem {} anos de idade e seu imc é {}'.format(nome,idade,imc))
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')