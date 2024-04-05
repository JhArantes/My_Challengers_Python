respostas_esperadas = ['*','x', '/', '+', '-', 'multiplicacao', 'divisao', 'adicao', 'subtracao']

parar = ''
while parar != 'S':
    
    num_1 = input('Numero: ')
    
    operador = input('operador: ').lower()
    if operador not in respostas_esperadas: 
        print('\n\nOperador não esperado\n')
        continue 
    num_2 = input(f'{num_1} {operador} ')
    
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except:
        print('Passe um numero!! ')
        continue

    if operador in ['x', '*', 'multiplicacao']:
        resultado = num_1  * num_2
    elif operador in ['/', 'divisao']:
        resultado = num_1 / num_2
    elif operador in ['+', 'adicao']:
        resultado = num_1 + num_2
    elif operador in ['-', 'subtracao']:
        resultado = num_1 - num_2
    
    print(resultado)
    
    
    
    
    parar = input('Quer parar?? [S/N]').upper()

print('Finalizado!! ')
