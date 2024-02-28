from random import choice #escolher lista
import os #limpar terminal

# Controle palavras
list_secrets_words = ['apple','working', 'cavalo', 'computador']
palavra_secreta = choice(list_secrets_words)
user_letras = []


print('-=' * 20)
print('Vamos jogar um jogo!!\nFale letras e direi se ela existe na palavra secreta ou não')
print('-=' * 20)




contador = 0
while True:
    contador += 1
    
    #pega letra
    letra_user = input("\nDigite uma letra: ").lower().strip()
    
    if letra_user == palavra_secreta:
        break
    # Apenas 1 
    if len(letra_user) > 1:
        print('Passe apenas uma letra')
        continue
    if letra_user in user_letras:
        print('Está letra já foi digitada')
        continue
    
    
    user_letras.append(letra_user)
    print('Secret Word: ', end='')
    for i in palavra_secreta:
        
        if i in user_letras:
            print(i, end='')
        elif i not in user_letras:
            print('*', end='')
            
    os.system('cls')

os.system('cls')

print('Você Ganhou!! com ', contador,' tentativas')



'''
    for p, i in enumerate(palavra_secreta):
        if i == letra_user:
            palavra_user[p] = i
        
        

    visao_palavra = ''.join(palavra_user)
    print(visao_palavra)
    contador += 1
    
    if palavra_secreta == palavra_user:
        break
'''  