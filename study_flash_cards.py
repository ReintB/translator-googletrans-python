import os
import ast
import random
import time

file_name = "flash_cards.txt"

def exit_if_cards_file_does_not_exist():
    if not os.path.exists(file_name):
        print("No cards available yet. Please first create new ones.")
        exit()

def retrive_cards_from_file():
    cards = []
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            cards = ast.literal_eval(f.read())
    return cards

def guess_cards():
    global cards
    while len(cards) > 0:
        index = random.randint(0, len(cards) - 1)
        word_en = cards[index][0]
        word_id = cards[index][1]
        answer = input(word_en + "? ")
        if answer == word_id:
            print("Correct!")
            del cards[index]
        else:
            print("Not correct. Will retry later.")

exit_if_cards_file_does_not_exist()
cards = retrive_cards_from_file()
print("You have " + str(len(cards)) + " cards to guess.")
input("Ready? Press ENTER to start.")
time_begin = time.time()
guess_cards()
time_end = time.time()
duration = int(time_end - time_begin)
print("You guessed all the cards in " + str(duration) + " seconds.")
print("End of program.")