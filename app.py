from random import choice
import json


with open('words.json', encoding='UTF-8') as f:
    wordlist = json.load(f)
    word = choice(wordlist)
    print(word)

