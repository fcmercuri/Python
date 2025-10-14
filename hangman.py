import random
import os
import time
list_of_words = ["Apple", "Banana", "Grapes", "Orange", "Mango"]
lives = 6
letters_picked = []
chosen_word = random.choice(list_of_words)
while True:
    time.sleep(1)
    # Clear screen in a cross-platform way
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("Current word: ", end="")
    allLetter = True
    for i in chosen_word.lower():
        if i in letters_picked:
            print(i, end=" ")
        else:
            print("_", end=" ")
            allLetter = False
    print()

    if allLetter:
        print(f"You won with {lives} lives left!")
        break

    if lives <= 0:
        print("You lost the game, the word was", chosen_word)
        break

    letter = input("Guess a letter: ").lower()
    if not letter.isalpha() or len(letter) != 1:
        print("Please enter a single alphabetic character.")
        time.sleep(1)
        continue

    if letter in letters_picked:
        print("You already guessed that letter. Try again.")
        time.sleep(1)
        continue

    letters_picked.append(letter)

    if letter in chosen_word.lower():
        print("Correct guess!")
    else:
        print("Wrong guess!")
        lives -= 1
        print(f"You have {lives} lives left")
        time.sleep(1)
