from random import choice
import os
import json
import time

play = True


wrong_letters_list = []
wrong_guess_count = 0
os.system('cls' if os.name == 'nt' else 'clear')

def word_selection():
    with open('words.json', encoding='UTF-8') as f:
        wordlist = json.load(f)
        word = choice(wordlist)
        #word = wordlist[1]

        word_playing = list(word)

        guessed_word = ["_"] * len(word)
    return(word_playing, guessed_word, word)

word_playing, guessed_word, word = word_selection()

while play:


    print(wrong_guess_count)
    if wrong_guess_count == 10:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Jadu nu dog du och hänger du. Ordet va: {word}")
        print("Score: <PLACEHOLDERSCORE>")
        play_again_input = input("Vill du spela igen? Y/N ").lower()
        if play_again_input == "y":
            wrong_letters_list = []
            wrong_guess_count = 0
            play = True
            word_playing, guessed_word, word = word_selection()
        else:
            play = False
            break

    if guessed_word == word_playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Du gissade ordet rätt!!")
        play_again_input = input("Vill du spela igen? Y/N ").lower()
        if play_again_input == "y":
            wrong_letters_list = []
            wrong_guess_count = 0
            play = True
            word_playing, guessed_word, word = word_selection()
        else:
            play = False
            break



    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(guessed_word)
        print(f"Fel gissade bokstaver: {wrong_letters_list}")
        print(f"Du har {10 - wrong_guess_count} försök kvar!")
        player_guess = input("Gissa en Bokstav: ").lower()
        if len(player_guess) > 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nNej du bara en bokstav')
            time.sleep(1)
        else:
            if player_guess in wrong_letters_list:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nDen här bokstaven har du redan gissat fel!")
                time.sleep(1)

                
            else:
                try:
                    word_playing.index(player_guess)
                    for i, letter in enumerate(word_playing):

                        if player_guess == letter:

                            guessed_word[i] = player_guess
                        
                except ValueError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    wrong_guess_count += 1
                    print("\nDen där bokstaven var FEL!\n")
                    wrong_letters_list.append(player_guess)
                    time.sleep(1)


            




            


    



