import asyncio
from googletrans import Translator
import os, ast

translator = Translator()
cards = []
file_name = "flash_cards.txt"

async def translate_word(word_en):
    result = await translator.translate(word_en, src="en", dest="id")
    return result.text

def retrive_cards_from_file():
    cards = []
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            cards = ast.literal_eval(f.read())
    return cards

def display_cards(cards):
    print("The current card list contains " + str(len(cards)) + " cards.")
    for i, card in enumerate(cards):
        print(f"{i+1}. {card[0]}: {card[1]}")

async def create_new_card():
    global cards
    word_en = input("Enter an English word: ")
    word_id = await translate_word(word_en)
    new_card = (word_en, word_id)
    print(new_card)
    answer = input("Do you want to save this card? (y/n): ")
    if answer.lower() == 'y':
        cards.append(new_card)

def save_cards_to_file():
    answer = input("Do you want to save all cards to file? (y/n): ")
    if answer.lower() == 'y':
        print("Saving cards to file...")
        with open(file_name, "w") as f:
            f.write(str(cards))

async def main():
    global cards
    cards = retrive_cards_from_file()
    display_cards(cards)
    while True:
        await create_new_card()
        answer = input("Do you want to translate another word? (y/n): ")
        if answer.lower() == 'n':
            break
    print(cards)
    save_cards_to_file()
    print("Program ended.")

if __name__ == "__main__":
    asyncio.run(main())