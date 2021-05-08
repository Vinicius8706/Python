numero = input("Digite um número: ")
numero_int = int(numero)
if numero_int % 2 == 0 :
    print('É par')
else:
    print('É ímpar')

hora = input('Digite a hora: ')
minuto = input('Digite o minuto: ')

if hora.isdigit():
    hora = int(hora)
    
    if hora < 0 or hora >23:
        print('Horario deve estar entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom dia')
        elif hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Por favor, digite um horario entre 0 e 23.')

print(f"Bom dia {hora}-{minuto}")

nome = input('Insire seu primeiro nome: ')
if nome.__len__() <= 4:
    print('Seu nome é curto')
elif len(nome) > 4 and len(nome) <= 5:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
