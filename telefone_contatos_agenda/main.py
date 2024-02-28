
# Agenda de contatos
def mostraContatos():
    for key, value in lista_contatos.items():
            print(' ')
            print(key, ' -> ', value)


lista_contatos = {'Policia' : 901, 'Samu' : 902}



while True:
    print('-=' * 20)
    user = input('Bem vindo ao seu celular!!! \n'
                 '\n'
                 'O que deseja fazer hoje?? \n'
                 '[ 1 ] Novos contatos \n'
                 '[ 2 ] Ver todos os contatos\n'
                 '[ 3 ] Ligar para um contato\n'
                 '[ 4 ] Sair do celular\n  ').strip()
    print('-=' * 20)
    # Verifica se o valor passado pelo user é valido
    if user not in '1234':
        print('Digite uma entrada valida!! ')
        continue
    
    #Sair do telefone
    if user == '4':break

    #adiciona contato
    if user == '1':
        key_new_contato = input('Nome: ')
        value_new_contato = input('Numero: ')
        
        #Verifica se com os valores passados pode ser criado um contato
        if len(value_new_contato) < 8 or key_new_contato.isdecimal():
            print('Você passou falores errados, recomece! ')
            continue
        # Adiciona o novo contato a lista de contatos
        novo_contato = {key_new_contato : value_new_contato}
        lista_contatos.update(novo_contato)
        continue
    
    #Mostra os contatos
    elif user == '2':
        mostraContatos()
    
    # Mostra os contatos e "liga" para eles
    elif user == '3':
        print('Central de ligações!')
        mostraContatos()
        print('-=' * 22)
        
        ligar = input('\n\nPara quem deseja ligar: \n ')
        
        print('\n\n Numero: ', lista_contatos[ligar])
        
        print('  Chamando...')
print('Você Saiu, Volte sempre!!')