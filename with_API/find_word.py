import requests
import os
from random import choice 

r = requests.get('https://www.randomlists.com/data/words.json').json()
word = choice(r['data']).upper()

print('-=' * 20)
print('Lets go play one game!!\nSay letters that you think are in the secret word!!')
print('-=' * 20)

correct_letter = []
score = 0
while True:
    user_letter = input('\nGuess letter: \n').upper().strip()
    
    if user_letter == word:
        break
    if len(user_letter) > 1 or not user_letter.isalpha():
        print('Please, valid entry')
        continue
    if user_letter in correct_letter:
        print('This letter has already been typed')
        continue
    
    if user_letter in word:
        correct_letter.append(user_letter)
        print('\nCurrent Word:', end=' ')
        for i in word:
            if i in correct_letter:
                print(i, end='')
            else:
                print('-', end='')
    else:
        print('Incorrect guess!')
        
    if set(word) <= set(correct_letter):
        break
    score += 1


os.system('cls')

print('\nCongratulations! You won with', score,'attempt!!')