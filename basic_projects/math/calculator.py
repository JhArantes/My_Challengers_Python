from datetime import datetime

# Estilizar o codigo 
def lin(msg):
    print('-=' * 20)
    print(msg)
    print('-=' * 20)

# O que dizer ao usuário
hour = datetime.now().hour
if hour < 12:
    user_hour = 'Bom dia'
elif 18 > hour > 12:
    user_hour = 'Boa tarde'
else: 
    user_hour = 'Boa noite'

# Cumprimentando usuário
lin(f'{user_hour}')

respostas_esperadas = ['*', '/', '+', '-', 'multiplicacao', 'divisao', 'adicao', 'subtracao']
while True:
    user_operador = input('''Qual tabuada deseja??\n
                        [ * ] Multiplicação\n
                        [ / ] Divisão\n
                        [ + ] Adição\n
                        [ - ] Subtração''').lower()

    if user_operador not in respostas_esperadas:
        lin('\nEscreva uma entrada válida\n ')
        continue

    user_numero = input('Numero da tabuada: ')
    
    try:
        user_numero = int(user_numero)
    except:
        lin('\nDigite um número!!\n ')
        continue
    
    for i in range(0, 11):
        if user_operador in ['*', 'multiplicacao']:
            operador = user_numero * i
        elif user_operador in ['/', 'divisao']:
            operador = user_numero / i
        elif user_operador in ['+', 'adicao']:
            operador = user_numero + i
        elif user_operador in ['-', 'subtracao']:
            operador = user_numero - i
        
        print(f'{user_numero} {user_operador} {i} = {abs(operador)}')
        
    keep = input('Quer continuar?? [S/N]').upper()
    if keep == 'N':
        break

print(f'Programa finalizado!! Tenha uma ótima {user_hour[4:]}')
