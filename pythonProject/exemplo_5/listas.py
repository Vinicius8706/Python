""" 
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min,max,
range
"""

# texto  = 'Valor'
# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# lista[5] = 'Qualquer outra coisa'
# print(lista[::2])

# print(lista[5])

# l1 = [1, 2, 3]
# l2 = [4,5,6]
# l1.extend(l2)
# l2.insert(0, 'banana')

# print(l1)
# l2.pop()
# print(l2)

# l2 = ['String', True,10, -20.5]
# for valor in l2:
 # print(f'O tipo de elemento é {type(valor)} e seu valor é {valor}')
# print(l2)
digitadas = []
secreto = 'perfume'
chances = 3

while True:
  letra = input('Digite uma letra: ')
  
  if len(letra) > 1:
    print('Ahhh isso não vale, digite apenas uma letra')
    continue
  
  digitadas.append(letra)
  
  if letra in secreto:
    print(f'UHULLL, a letra "{letra}" existe na palavra secreta')
    
  else:
    print(f'Afffz a letra "{letra}" NÃO existe na palavra secreta')    
    digitadas.pop()
    
  secreto_temporario = ''
  for letra_secreta in secreto:
    if letra_secreta in digitadas:
      secreto_temporario += letra_secreta
    else:
      secreto_temporario += '*'

  if secreto_temporario == secreto:
    print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
    break
  else:
    print(f'A palavra secreta está assim: {secreto_temporario}')

  if letra not in secreto:
      chances -= 1
  print(f'Voce ainda tem {chances} chances')

      
