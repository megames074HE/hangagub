from random import choice
import json


with open('words.json', encoding='UTF-8') as f:
    wordlist = json.load(f)
    #word = choice(wordlist['ord'])
    word = wordlist[1]

    word_playing = list(word)

    print(word_playing)

    guessed_letters = ["_"] * len(word)

    print(guessed_letters)

    player_guess = ""
    
    player_guess_letter = list(player_guess)

    for i, letter in enumerate(word_playing):

        if letter in player_guess_letter:
            print(f"hittade: {letter}, plats: {i}")
            guessed_letters[i] = letter
    
            

print(guessed_letters)