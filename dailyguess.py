import requests
import random
import string


correctletter = {}

for i in range(5):
    correctletter[i]  = '#'

while True: 
    word = random.choices(string.ascii_lowercase, k=5)
    
    for i in range(5):
        if correctletter[i] != '#':
            word[i] = correctletter[i]

   
    word = ''.join(word)
    
    urlword = f'https://wordle.votee.dev:8000/daily'
    params={'guess':word}
    response=requests.get(urlword,params=params)
 
    lettercheck = response.json()
    correctdct = 0
    for dct in lettercheck:
        if dct['result'] == 'correct':
            if dct['guess'] == word[dct['slot']]:
                correctdct += 1
    print(f'correct letter so far: {correctdct} and word: {word}')
    


    for dct in lettercheck:
        if correctletter[dct['slot']] == '#':
            if dct['result'] == 'correct':
                correctletter[dct['slot']] = dct['guess']
      
    print(f'correctletter: {correctletter}')
    
    
    if correctdct == 5:
        print(f'Final word: {word}')
        break
