"""
For / Else em Python

"""

variavel = ['Vinicius Farias', 'Joãozinho', 'Maria']

comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        pass
        #continue

    print(valor)

else:
    print('Não existe uma palavra que começa com J')