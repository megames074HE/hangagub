from random import choice
import json

play = True

wrong_letters_list = []

with open('words.json', encoding='UTF-8') as f:
    wordlist = json.load(f)
    #word = choice(wordlist['ord'])
    word = wordlist[1]

    word_playing = list(word)

    print(word_playing)

    guessed_word = ["_"] * len(word)

while play:

    if guessed_word == word_playing:
        print("You guessed the word")
        play_again_input = input("Vill du spela igen? Y/N ").lower()
        if play_again_input == "y":
            play = True
        else:
            play = False
            break



    else:
        print(f"Fel gissade bokstaver: {wrong_letters_list}")
        player_guess = input("Gissa en Bokstav: ").lower()

        if player_guess in wrong_letters_list:
            print("\nDen här bokstaven har du redan gissat fel!")
            
        
        try:
            word_playing.index(player_guess)
            for i, letter in enumerate(word_playing):

                if player_guess == letter:

                    guessed_word[i] = player_guess
                

        except ValueError:

            print("\nDen där bokstaven var FEL!\n")
            wrong_letters_list.append(player_guess)


            




            


    

    print(guessed_word)


