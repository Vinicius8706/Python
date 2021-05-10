# contador = 1
# acumulador = 1

# while contador <= 10:
#   print(contador, acumulador)
  
#   if contador > 5:
#     break
  
#   acumulador = contador + acumulador
#   contador += 1
# else:
#   print('Cheguei no else')
# print('Isso será executado')

# #   Indíces
#    0123456789.............33...

frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_do_usuario = input('Qual letra deseja colocar maiúscula? ')

while contador < tamanho_frase:
  letra = frase[contador]
  if letra == input_do_usuario:
    nova_string += input_do_usuario.upper()
      
  else:
    nova_string += letra
  contador += 1
  
print(nova_string)
  