import os
import ast
import random
import time

file_name = "flash_cards.txt"

def exit_if_cards_file_does_not_exist():
  if not os.path.exists(file_name):
    print("Tidak ada kartu yang tersedia. Harap buat yang pertama.")
    exit()

def retrieve_cards_from_file():
  cards = []
  if os.path.exists(file_name):
    try:
      with open(file_name, "r") as f:
        content = f.read()
        if content:
          cards = ast.literal_eval(content)
    except Exception as e:
      print(f"Kesalahan dalam membaca file: {e}. Keluar dari program.")
      exit()

  return cards

def guess_cards(cards):
  while len(cards) > 0:
    index = random.randint(0, len(cards) - 1)
    word_en = cards[index][0]
    word_id = cards[index][1]

    answer_raw = input(word_en + "? ")

    normalized_answer = answer_raw.strip().lower()
    normalized_correct_id = word_id.strip().lower()

    if normalized_answer == normalized_correct_id:
      print("Benar!")
      del cards[index]
    else:
      print(f"Jawaban tidak tepat. Jawaban benar adalah: '{word_id}'. Coba ulangi lagi! ")

exit_if_cards_file_does_not_exist()
cards = retrieve_cards_from_file()
print("Kamu memiliki " + str(len(cards)) + " kartu untuk ditebak")
input("Siap? Tekan ENTER untuk memulai")
time_begin = time.time()
guess_cards(cards)
time_end = time.time()
duration = int(time_end - time_begin)
print("Kamu berhasil menebak seluruh kartu dalam " + str(duration) + " detik.")
print("Program selesai!")