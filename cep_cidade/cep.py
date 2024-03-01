import requests


def line():
    print('-=' * 22)



line()
cepi_user = input("Qual o numero do seu cep?? ")
line()

cep_r = requests.get(f'https://opencep.com/v1/{cepi_user}').json()

print('Você mora em: ', cep_r['localidade'], cep_r['uf'] )
line()


