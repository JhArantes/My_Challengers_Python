# Sorteia 1 numero do intervalo passado pelo user
from random import randint

print('-=' * 20)
print('Coloque o valor maximo e minimo e sortearei um numero neste intervalo')
print('-=' * 20)
maximo = int(input('Qual o valor maximo: '))
minimo = int(input('Qual o valor minimo: '))


numero = randint(minimo, maximo)

print(f'O numero sorteado foi {numero}')
 