import requests


def line():
    print('-=' * 22)



line()
cepi_user = input("Qual o numero do seu cep?? ")
line()

cep_r = requests.get(f'https://cep.awesomeapi.com.br/json/{cepi_user}')
cep_r = cep_r.json()

print('Você mora em: ', cep_r['city'], cep_r['state'] )
line()


