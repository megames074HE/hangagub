from random import choice
from visuals import art
from colorama import Fore, Style
import os
import json
import time

play = True

wrong_letters_list = []
wrong_guess_count = 0
points_current = 0


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def word_selection(player_difficulty):
    with open('words.json', encoding='UTF-8') as f:
        wordlist = json.load(f)
        word = choice(wordlist[player_difficulty])
        #word = wordlist[1]

        word_playing = list(word)

        guessed_word = ["_"] * len(word)
    return(word_playing, guessed_word, word)

def highscore(points_current, player_initials):
    with open('highscores.json', encoding='UTF-8') as f:
        highscore_data = json.load(f)
        highscore_points = highscore_data['score']
        highscore_initials = highscore_data['name']
        new_highscore = False


    if int(points_current) > int(highscore_points):
        with open('highscores.json', 'w') as f:
            json.dump({"score":points_current, "name":player_initials}, f)
            new_highscore = True
            highscore_points = points_current
            highscore_initials = player_initials
    
    return(highscore_points, new_highscore, highscore_initials)



def start_menu(points_current, player_initials):
    
    clear_screen()
    highscore_points, new_highscore, highscore_initials = highscore(points_current, player_initials)

    art(12)
    if new_highscore:
        print(Fore.GREEN ,f"\nGRATTIS!!! Du har fått ett nytt highscore! Ditt highscore: {highscore_points}. Det sparas nu! Du kan spela vidare för att få ett högre highscore.", Style.RESET_ALL)
        new_highscore = False
    else:
        print(Fore.YELLOW, f"\nHighscore: {highscore_points}, uppnådd av: {highscore_initials}", Style.RESET_ALL)
    if points_current > 0:
        print(Fore.BLUE, f"\nNuvarande poäng: {points_current}. Nuvarande spelare namn: {player_initials}", Style.RESET_ALL)
    print("\nVälkommen till Hänga Gubbe. Välj dina alternativ nedan")
    print("\nSkriv x för att lämna spelet.")
    print("\nSvårighet:")
    print("1: Lätt, kortare ord. 10 gissningar, du får poäng för antalet gissningar du har kvar.")
    print("2: Medelsvåra, något längre ord. Du får bara 8 gissningar. Men dubbla poäng")
    print("3: Svår, svåra långa ord. Du får bara 5 gissningar, men du får 3x poäng.")

    player_difficulty = input("\nVälj din svårighet [1-3]: ")

    if player_difficulty.lower() == "x":
        clear_screen()
        exit()

    if player_difficulty.isnumeric() == False or len(player_difficulty) > 1:
        clear_screen()
        print("\nDu kan bara ange en siffra!")
        time.sleep(1)
        return start_menu(0, 0)
    elif int(player_difficulty) > 3 or int(player_difficulty) < 1:
        clear_screen()
        print("\nVälj siffror 1 till 3!")
        time.sleep(1)
        return start_menu(0, 0)

    if player_initials == 0:

        player_initials = input("\nAnge din highscore namn: ").upper()

        if player_initials.lower() == "x":
            clear_screen()
            exit()

        if player_initials.isalpha() == False:
            clear_screen()
            print("\nAnge bara bokstäver. Inte siffror eller specialtecken!")
            time.sleep(1)
            return start_menu(0, 0)    

    return player_difficulty, player_initials

player_difficulty, player_initials = start_menu(0, 0)

word_playing, guessed_word, word = word_selection(player_difficulty)

while play:


    print(wrong_guess_count)
    if wrong_guess_count == 10:
        clear_screen()
        art(10)
        time.sleep(1.5)
    
        clear_screen()
        art(11)
        print(Fore.RED,f"Jadu nu dog du och hänger du. Ordet va: {word}", Style.RESET_ALL)
        print(f"Score: {points_current}")


        play_again_input = input("Vill du spela igen? [Y/N] ").lower()
        if play_again_input == "y":
            points_current = 0
            wrong_letters_list = []
            wrong_guess_count = 0
            play = True
            player_difficulty, player_initials = start_menu(0, 0)
            word_playing, guessed_word, word = word_selection(player_difficulty)
        else:
            clear_screen()
            play = False
            break

    if guessed_word == word_playing:
        clear_screen()
        if player_difficulty == 5:
            points_current += (10 - wrong_guess_count)*3
        elif player_difficulty == 4:
            points_current += (10 - wrong_guess_count)*2
        else:
            points_current += 10 - wrong_guess_count

        print(Fore.GREEN,"\nDu gissade ordet rätt!!", Style.RESET_ALL)
        print(f"Score: {points_current}")
        play_again_input = input("Vill du spela igen? [Y/N] ").lower()
        if play_again_input == "y":
            wrong_letters_list = []
            wrong_guess_count = 0
            play = True
            player_difficulty, player_initials = start_menu(points_current, player_initials)
            word_playing, guessed_word, word = word_selection(player_difficulty)
        else:
            clear_screen()
            highscore(points_current, player_initials)
            play = False
            break



    else:
        clear_screen()
        if int(player_difficulty) == 2:
            wrong_guess_count += 2
            player_difficulty = 4
        if int(player_difficulty) == 3:
            wrong_guess_count += 5
            player_difficulty = 5



        if int(player_difficulty) == 4:
            if wrong_guess_count != 2:
                art(wrong_guess_count)
        elif int(player_difficulty) == 5:
            if wrong_guess_count != 5:
                art(wrong_guess_count)
        else:
            art(wrong_guess_count)
        

        print('  '.join(guessed_word))
        print(f"Fel gissade bokstäver: {', '.join(wrong_letters_list)}")
        print(f"Du har {10 - wrong_guess_count} försök kvar!")
        player_guess = input("Gissa en Bokstav: ").lower()
        if len(player_guess) > 1:
            clear_screen()
            print('\nBara en bokstav, inte fler!')
            time.sleep(1)
        elif player_guess.isnumeric():
            clear_screen()
            print('\nBara bokstäver, inte siffror!')
            time.sleep(1)
        elif player_guess.isalpha() == False:
            clear_screen()
            print('\nBara bokstäver, inte specialtecken!')
            time.sleep(1)
        else:
            if player_guess in wrong_letters_list:
                clear_screen()
                print("\nDen här bokstaven har du redan gissat fel!")
                time.sleep(1)

                
            else:
                try:
                    word_playing.index(player_guess)
                    for i, letter in enumerate(word_playing):

                        if player_guess == letter:

                            guessed_word[i] = player_guess
                        
                except ValueError:
                    clear_screen()
                    wrong_guess_count += 1
                    print("\nDen där bokstaven var FEL!\n")
                    wrong_letters_list.append(player_guess)
                    time.sleep(1)


            


    



