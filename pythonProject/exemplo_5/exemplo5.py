# x = 0
# while x < 5:
#   if x == 3:
#     x = x + 1
#     break
  
#   print(x)
#   x = x + 1
  
# print("Acabou")

while True:
  print()
  num_1 = input("Digite um numero: ")
  num_2 = input("Digite outro numero: ")
  operador = input("Digite um operador: ")
  sair = input('Deseja sair [s]sim ou [n] não: ')
  
  if sair == 's':
    break
  
  if not num_1.isnumeric() or not num_2.isnumeric():
    print("Voce precisa digitar um numero")
    continue
  
  num_1 = int(num_1)
  num_2 = int(num_2)
  if operador == '+':
    print(num_1 + num_2)
  elif operador == '-':
    print(num_1 - num_2)
  elif operador == '/':
    print(num_1 / num_2)
  elif operador == '*':
    print(num_1 * num_2)
  else:
    print('Operador inválido')
  
  