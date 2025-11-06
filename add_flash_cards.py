import asyncio
from googletrans import Translator
import os, ast

translator = Translator()
cards = []
file_name = "flash_cards.txt"

async def translate_word(word_en):
  try:
    result = await translator.translate(word_en, src="en", dest="id")
    return result.text
  except Exception as e:
    print(f"Gagal menerjemahkan: {e}. Menggunakan kata asli sebagai terjemahan.")
    return word_en

def retrieve_cards_from_file():
  cards = []
  if os.path.exists(file_name):
    try:
      with open(file_name, "r") as f:
        content = f.read()
        if content:
          cards = ast.literal_eval(content)
    except Exception as e:
      print(f"Peringatan: File kartu mungkin rusak atau kosong. Membuat kartu kosong. {e}")
      cards = []
  return cards

def display_cards(cards):
  print("List kartu sementara berisikan " + str(len(cards)) + " kartu")
  for i, card in enumerate(cards):
    print(f"{i+1}. {card[0]}: {card[1]}")

async def create_new_card():
  global cards
  while True:
    word_en_raw = input("Masukkan satu kata dalam bahasa Inggris: ")
    word_en = word_en_raw.strip()
    if not word_en:
      print("Kata tidak boleh kosong. Silakan coba lagi")
      continue
    break

  print(f"Mencoba menerjemahkan `{word_en}`...")
  word_id = await translate_word(word_en)
  new_card = (word_en, word_id)
  print(new_card)

  answer = input("Apakah anda ingin menyimpan kartu ini? (y/n): ")
  if answer.lower() == 'y':
    cards.append(new_card)

def save_cards_to_file():
  global cards
  answer = input("Apakah anda ingin menyimpan semua kartu ke file? (y/n): ")
  if answer.lower() == 'y':
    print("Menyimpan kartu ke file...")
    try:
      with open(file_name, "w") as f:
        f.write(str(cards))
    except Exception as e:
      print(f"Gagal menyimpan ke file: {e}")

async def main():
  global cards
  cards = retrieve_cards_from_file()
  display_cards(cards)

  while True:
    await create_new_card()
    answer = input("Apakah anda ingin menerjemahkan kata lain? (y/n): ")
    if answer.lower() == 'n':
      break

  print(cards)
  save_cards_to_file()
  print("Program selesai.")

if __name__ == "__main__":
  asyncio.run(main())