# Dokumentasi Kode Flash Cards Translator

Dokumen ini menjelaskan secara detail setiap baris kode pada file `add_flash_cards.py` dan `study_flash_cards.py`, serta hubungan antara kedua file tersebut.

---

## Hubungan Antara Kedua File

Kedua file ini bekerja bersama dalam sistem pembelajaran bahasa Inggris-Indonesia menggunakan flash cards:

1. **`add_flash_cards.py`**: File ini digunakan untuk **membuat dan menyimpan** flash cards baru ke dalam file `flash_cards.txt`
2. **`study_flash_cards.py`**: File ini digunakan untuk **membaca dan mempelajari** flash cards yang sudah disimpan di `flash_cards.txt`

**Alur Kerja:**
```
add_flash_cards.py → flash_cards.txt → study_flash_cards.py
     (Membuat)          (Penyimpanan)        (Mempelajari)
```

Kedua file menggunakan file yang sama (`flash_cards.txt`) sebagai media penyimpanan data, sehingga kartu yang dibuat di `add_flash_cards.py` dapat dipelajari di `study_flash_cards.py`.

---

## Penjelasan File: `add_flash_cards.py`

File ini bertanggung jawab untuk membuat flash cards baru dengan menerjemahkan kata bahasa Inggris ke bahasa Indonesia menggunakan Google Translate API.

### Import dan Inisialisasi

```python
import asyncio
```
**Baris 1**: Mengimpor modul `asyncio` untuk mendukung operasi asynchronous (non-blocking). Diperlukan karena Google Translate API menggunakan operasi async.

```python
from googletrans import Translator
```
**Baris 2**: Mengimpor kelas `Translator` dari library `googletrans` yang digunakan untuk menerjemahkan teks.

```python
import os, ast
```
**Baris 3**: 
- `os`: Digunakan untuk operasi sistem file (mengecek keberadaan file)
- `ast`: Digunakan untuk mengevaluasi string Python menjadi objek Python (untuk membaca data dari file)

```python
translator = Translator()
```
**Baris 5**: Membuat instance objek `Translator` yang akan digunakan untuk menerjemahkan kata-kata.

```python
cards = []
```
**Baris 6**: Inisialisasi variabel global `cards` sebagai list kosong untuk menyimpan flash cards sementara dalam memori.

```python
file_name = "flash_cards.txt"
```
**Baris 7**: Menentukan nama file yang digunakan untuk menyimpan flash cards. File ini akan dibaca dan ditulis oleh kedua program.

### Fungsi `translate_word()`

```python
async def translate_word(word_en):
```
**Baris 9**: Mendefinisikan fungsi async `translate_word` yang menerima parameter `word_en` (kata dalam bahasa Inggris). Fungsi ini async karena operasi translate membutuhkan waktu.

```python
  try:
```
**Baris 10**: Memulai blok try-except untuk menangani error yang mungkin terjadi saat menerjemahkan.

```python
    result = await translator.translate(word_en, src="en", dest="id")
```
**Baris 11**: 
- `await`: Menunggu operasi translate selesai (karena async)
- `translator.translate()`: Memanggil fungsi translate dengan parameter:
  - `word_en`: Kata yang akan diterjemahkan
  - `src="en"`: Bahasa sumber (English)
  - `dest="id"`: Bahasa tujuan (Indonesian)
- Hasil disimpan di variabel `result`

```python
    return result.text
```
**Baris 12**: Mengembalikan teks terjemahan dari objek result.

```python
  except Exception as e:
```
**Baris 13**: Menangkap semua jenis exception yang mungkin terjadi (misalnya koneksi internet terputus, API error, dll).

```python
    print(f"Gagal menerjemahkan: {e}. Menggunakan kata asli sebagai terjemahan.")
```
**Baris 14**: Mencetak pesan error yang informatif kepada pengguna.

```python
    return word_en
```
**Baris 15**: Jika terjadi error, mengembalikan kata asli (bahasa Inggris) sebagai fallback, sehingga program tetap dapat berjalan.

### Fungsi `retrieve_cards_from_file()`

```python
def retrieve_cards_from_file():
```
**Baris 17**: Mendefinisikan fungsi untuk membaca flash cards yang sudah ada dari file.

```python
  cards = []
```
**Baris 18**: Inisialisasi list kosong untuk menyimpan kartu yang dibaca dari file.

```python
  if os.path.exists(file_name):
```
**Baris 19**: Mengecek apakah file `flash_cards.txt` ada di sistem file.

```python
    try:
```
**Baris 20**: Memulai blok try-except untuk menangani error saat membaca file.

```python
      with open(file_name, "r") as f:
```
**Baris 21**: Membuka file dalam mode read (`"r"`). Menggunakan `with` statement untuk memastikan file ditutup otomatis setelah selesai.

```python
        content = f.read()
```
**Baris 22**: Membaca seluruh isi file dan menyimpannya ke variabel `content`.

```python
        if content:
```
**Baris 23**: Mengecek apakah file tidak kosong.

```python
          cards = ast.literal_eval(content)
```
**Baris 24**: 
- `ast.literal_eval()`: Mengevaluasi string Python menjadi objek Python dengan aman
- Mengkonversi string yang dibaca dari file menjadi list of tuples (format flash cards)
- Lebih aman daripada `eval()` karena hanya mengevaluasi literal Python

```python
    except Exception as e:
```
**Baris 25**: Menangkap error yang mungkin terjadi (misalnya format file tidak valid).

```python
      print(f"Peringatan: File kartu mungkin rusak atau kosong. Membuat kartu kosong. {e}")
```
**Baris 26**: Mencetak peringatan jika terjadi error, tetapi program tetap berjalan.

```python
      cards = []
```
**Baris 27**: Menginisialisasi list kosong jika terjadi error, sehingga program tetap dapat berjalan.

```python
  return cards
```
**Baris 28**: Mengembalikan list kartu yang berhasil dibaca (atau list kosong jika file tidak ada/error).

### Fungsi `display_cards()`

```python
def display_cards(cards):
```
**Baris 30**: Mendefinisikan fungsi untuk menampilkan semua kartu ke layar.

```python
  print("List kartu sementara berisikan " + str(len(cards)) + " kartu")
```
**Baris 31**: Mencetak jumlah total kartu yang ada.

```python
  for i, card in enumerate(cards):
```
**Baris 32**: Loop melalui setiap kartu dengan menggunakan `enumerate()` untuk mendapatkan index dan nilai kartu.

```python
    print(f"{i+1}. {card[0]}: {card[1]}")
```
**Baris 33**: Mencetak setiap kartu dalam format "nomor. kata_inggris: kata_indonesia". `card[0]` adalah kata Inggris, `card[1]` adalah kata Indonesia.

### Fungsi `validate_yes_no_input()`

```python
def validate_yes_no_input(prompt):
```
**Baris 35**: Mendefinisikan fungsi untuk memvalidasi input y/n dari pengguna.

```python
  """Memvalidasi input y/n dan mengembalikan True untuk 'y' dan False untuk 'n'"""
```
**Baris 36**: Docstring yang menjelaskan fungsi.

```python
  while True:
```
**Baris 37**: Loop tak terbatas yang akan terus meminta input sampai valid.

```python
    answer = input(prompt).strip().lower()
```
**Baris 38**: 
- `input(prompt)`: Meminta input dari pengguna dengan prompt tertentu
- `.strip()`: Menghapus spasi di awal dan akhir
- `.lower()`: Mengubah ke huruf kecil untuk perbandingan yang tidak case-sensitive

```python
    if answer == 'y' or answer == 'yes':
```
**Baris 39**: Mengecek apakah jawaban adalah 'y' atau 'yes'.

```python
      return True
```
**Baris 40**: Mengembalikan `True` jika pengguna menjawab ya.

```python
    elif answer == 'n' or answer == 'no':
```
**Baris 41**: Mengecek apakah jawaban adalah 'n' atau 'no'.

```python
      return False
```
**Baris 42**: Mengembalikan `False` jika pengguna menjawab tidak.

```python
    else:
```
**Baris 43**: Jika input tidak valid (bukan y/yes/n/no).

```python
      print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")
```
**Baris 44**: Mencetak pesan error dan loop akan berlanjut untuk meminta input lagi.

### Fungsi `create_new_card()`

```python
async def create_new_card():
```
**Baris 46**: Mendefinisikan fungsi async untuk membuat kartu baru.

```python
  global cards
```
**Baris 47**: Mendeklarasikan bahwa akan menggunakan variabel global `cards`.

```python
  while True:
```
**Baris 48**: Loop untuk memastikan input kata tidak kosong.

```python
    word_en_raw = input("Masukkan satu kata dalam bahasa Inggris: ")
```
**Baris 49**: Meminta input kata bahasa Inggris dari pengguna.

```python
    word_en = word_en_raw.strip()
```
**Baris 50**: Menghapus spasi di awal dan akhir input.

```python
    if not word_en:
```
**Baris 51**: Mengecek apakah input kosong setelah di-strip.

```python
      print("Kata tidak boleh kosong. Silakan coba lagi")
```
**Baris 52**: Mencetak pesan error jika input kosong.

```python
      continue
```
**Baris 53**: Melanjutkan loop untuk meminta input lagi.

```python
    break
```
**Baris 54**: Keluar dari loop jika input valid.

```python
  print(f"Mencoba menerjemahkan `{word_en}`...")
```
**Baris 56**: Memberi tahu pengguna bahwa proses translate sedang berlangsung.

```python
  word_id = await translate_word(word_en)
```
**Baris 57**: Memanggil fungsi `translate_word()` dan menunggu hasilnya. Hasil terjemahan disimpan di `word_id`.

```python
  new_card = (word_en, word_id)
```
**Baris 58**: Membuat tuple baru yang berisi pasangan kata (Inggris, Indonesia). Tuple digunakan karena data tidak akan berubah.

```python
  print(new_card)
```
**Baris 59**: Menampilkan kartu yang baru dibuat kepada pengguna.

```python
  if validate_yes_no_input("Apakah anda ingin menyimpan kartu ini? (y/n): "):
```
**Baris 61**: Memvalidasi input pengguna apakah ingin menyimpan kartu. Fungsi akan terus meminta sampai mendapat input valid.

```python
    cards.append(new_card)
```
**Baris 62**: Menambahkan kartu baru ke list `cards` jika pengguna memilih 'y'.

### Fungsi `save_cards_to_file()`

```python
def save_cards_to_file():
```
**Baris 64**: Mendefinisikan fungsi untuk menyimpan semua kartu ke file.

```python
  global cards
```
**Baris 65**: Mendeklarasikan penggunaan variabel global `cards`.

```python
  if validate_yes_no_input("Apakah anda ingin menyimpan semua kartu ke file? (y/n): "):
```
**Baris 66**: Memvalidasi input pengguna apakah ingin menyimpan ke file.

```python
    print("Menyimpan kartu ke file...")
```
**Baris 67**: Memberi tahu pengguna bahwa proses penyimpanan sedang berlangsung.

```python
    try:
```
**Baris 68**: Memulai blok try-except untuk menangani error saat menulis file.

```python
      with open(file_name, "w") as f:
```
**Baris 69**: Membuka file dalam mode write (`"w"`). File akan dibuat jika belum ada, atau ditimpa jika sudah ada.

```python
        f.write(str(cards))
```
**Baris 70**: Menulis list kartu ke file sebagai string. `str(cards)` mengkonversi list menjadi string Python literal.

```python
      print("Kartu berhasil disimpan ke file.")
```
**Baris 71**: Mencetak pesan sukses setelah file berhasil ditulis.

```python
    except Exception as e:
```
**Baris 72**: Menangkap error yang mungkin terjadi (misalnya permission denied, disk full, dll).

```python
      print(f"Gagal menyimpan ke file: {e}")
```
**Baris 73**: Mencetak pesan error yang informatif.

### Fungsi `main()`

```python
async def main():
```
**Baris 75**: Mendefinisikan fungsi async utama yang mengatur alur program.

```python
  global cards
```
**Baris 76**: Mendeklarasikan penggunaan variabel global `cards`.

```python
  cards = retrieve_cards_from_file()
```
**Baris 77**: Memuat kartu yang sudah ada dari file ke dalam variabel `cards`.

```python
  display_cards(cards)
```
**Baris 78**: Menampilkan semua kartu yang sudah dimuat.

```python
  while True:
```
**Baris 80**: Loop utama untuk membuat kartu baru berulang kali.

```python
    await create_new_card()
```
**Baris 81**: Membuat kartu baru. `await` digunakan karena fungsi ini async.

```python
    if not validate_yes_no_input("Apakah anda ingin menerjemahkan kata lain? (y/n): "):
```
**Baris 82**: Memvalidasi apakah pengguna ingin membuat kartu lagi. Jika jawaban 'n', kondisi akan `True` dan loop akan berhenti.

```python
      break
```
**Baris 83**: Keluar dari loop jika pengguna memilih 'n'.

```python
  print(cards)
```
**Baris 85**: Menampilkan semua kartu yang telah dibuat dalam sesi ini.

```python
  save_cards_to_file()
```
**Baris 86**: Menyimpan semua kartu ke file.

```python
  print("Program selesai.")
```
**Baris 87**: Mencetak pesan bahwa program telah selesai.

### Entry Point

```python
if __name__ == "__main__":
```
**Baris 89**: Mengecek apakah file ini dijalankan langsung (bukan diimpor sebagai modul).

```python
  asyncio.run(main())
```
**Baris 90**: Menjalankan fungsi `main()` menggunakan event loop asyncio. Ini diperlukan karena `main()` adalah fungsi async.

---

## Penjelasan File: `study_flash_cards.py`

File ini digunakan untuk mempelajari flash cards yang sudah dibuat dengan cara menebak terjemahan kata-kata.

### Import dan Konstanta

```python
import os
```
**Baris 1**: Mengimpor modul `os` untuk operasi sistem file (mengecek keberadaan file).

```python
import ast
```
**Baris 2**: Mengimpor modul `ast` untuk mengevaluasi string Python menjadi objek Python.

```python
import random
```
**Baris 3**: Mengimpor modul `random` untuk memilih kartu secara acak saat belajar.

```python
import time
```
**Baris 4**: Mengimpor modul `time` untuk mengukur waktu yang dibutuhkan untuk menyelesaikan semua kartu.

```python
file_name = "flash_cards.txt"
```
**Baris 6**: Menentukan nama file yang sama dengan `add_flash_cards.py` untuk membaca flash cards.

### Fungsi `exit_if_cards_file_does_not_exist()`

```python
def exit_if_cards_file_does_not_exist():
```
**Baris 8**: Mendefinisikan fungsi untuk memastikan file flash cards ada sebelum program berjalan.

```python
  if not os.path.exists(file_name):
```
**Baris 9**: Mengecek apakah file `flash_cards.txt` tidak ada.

```python
    print("Tidak ada kartu yang tersedia. Harap buat yang pertama.")
```
**Baris 10**: Mencetak pesan error yang informatif.

```python
    exit()
```
**Baris 11**: Menghentikan program karena tidak ada kartu yang bisa dipelajari.

### Fungsi `retrieve_cards_from_file()`

```python
def retrieve_cards_from_file():
```
**Baris 13**: Mendefinisikan fungsi untuk membaca flash cards dari file. **Fungsi ini identik dengan fungsi yang sama di `add_flash_cards.py`**.

```python
  cards = []
```
**Baris 14**: Inisialisasi list kosong untuk menyimpan kartu.

```python
  if os.path.exists(file_name):
```
**Baris 15**: Mengecek apakah file ada.

```python
    try:
```
**Baris 16**: Memulai blok try-except.

```python
      with open(file_name, "r") as f:
```
**Baris 17**: Membuka file dalam mode read.

```python
        content = f.read()
```
**Baris 18**: Membaca seluruh isi file.

```python
        if content:
```
**Baris 19**: Mengecek apakah file tidak kosong.

```python
          cards = ast.literal_eval(content)
```
**Baris 20**: Mengevaluasi string menjadi list of tuples.

```python
    except Exception as e:
```
**Baris 21**: Menangkap error.

```python
      print(f"Kesalahan dalam membaca file: {e}. Keluar dari program.")
```
**Baris 22**: Mencetak pesan error.

```python
      exit()
```
**Baris 23**: Menghentikan program karena file tidak dapat dibaca (berbeda dengan `add_flash_cards.py` yang tetap melanjutkan).

```python
  return cards
```
**Baris 25**: Mengembalikan list kartu.

### Fungsi `validate_guess_input()`

```python
def validate_guess_input(prompt):
```
**Baris 27**: Mendefinisikan fungsi untuk memvalidasi input tebakan pengguna.

```python
  """Memvalidasi input tebakan, memastikan tidak kosong"""
```
**Baris 28**: Docstring yang menjelaskan fungsi.

```python
  while True:
```
**Baris 29**: Loop tak terbatas sampai mendapat input valid.

```python
    answer = input(prompt).strip()
```
**Baris 30**: Meminta input dan menghapus spasi di awal/akhir.

```python
    if answer:
```
**Baris 31**: Mengecek apakah input tidak kosong.

```python
      return answer
```
**Baris 32**: Mengembalikan input jika valid.

```python
    else:
```
**Baris 33**: Jika input kosong.

```python
      print("Input tidak boleh kosong. Silakan masukkan jawaban Anda.")
```
**Baris 34**: Mencetak pesan error dan loop akan berlanjut.

### Fungsi `guess_cards()`

```python
def guess_cards(cards):
```
**Baris 36**: Mendefinisikan fungsi utama untuk proses belajar dengan menebak kartu.

```python
  while len(cards) > 0:
```
**Baris 37**: Loop akan berlanjut selama masih ada kartu yang belum ditebak dengan benar.

```python
    index = random.randint(0, len(cards) - 1)
```
**Baris 38**: Memilih index acak dari 0 sampai panjang list - 1. Ini membuat urutan belajar menjadi acak.

```python
    word_en = cards[index][0]
```
**Baris 39**: Mengambil kata bahasa Inggris dari kartu yang dipilih. `cards[index]` adalah tuple, `[0]` adalah elemen pertama (kata Inggris).

```python
    word_id = cards[index][1]
```
**Baris 40**: Mengambil kata bahasa Indonesia dari kartu yang dipilih. `[1]` adalah elemen kedua (kata Indonesia).

```python
    answer_raw = validate_guess_input(word_en + "? ")
```
**Baris 42**: Meminta tebakan dari pengguna dengan memvalidasi bahwa input tidak kosong. Prompt adalah kata Inggris diikuti tanda tanya.

```python
    normalized_answer = answer_raw.strip().lower()
```
**Baris 44**: 
- `.strip()`: Menghapus spasi di awal/akhir
- `.lower()`: Mengubah ke huruf kecil
- Ini membuat perbandingan tidak case-sensitive dan mengabaikan spasi

```python
    normalized_correct_id = word_id.strip().lower()
```
**Baris 45**: Menormalisasi jawaban yang benar dengan cara yang sama.

```python
    if normalized_answer == normalized_correct_id:
```
**Baris 47**: Membandingkan tebakan yang sudah dinormalisasi dengan jawaban yang benar.

```python
      print("Benar!")
```
**Baris 48**: Mencetak pesan sukses jika tebakan benar.

```python
      del cards[index]
```
**Baris 49**: Menghapus kartu dari list jika sudah ditebak dengan benar. Kartu ini tidak akan muncul lagi.

```python
    else:
```
**Baris 50**: Jika tebakan salah.

```python
      print(f"Jawaban tidak tepat. Jawaban benar adalah: '{word_id}'. Coba ulangi lagi! ")
```
**Baris 51**: Mencetak pesan error yang menunjukkan jawaban yang benar. Kartu tetap ada di list sehingga akan muncul lagi nanti.

### Program Utama (Script Level)

```python
exit_if_cards_file_does_not_exist()
```
**Baris 53**: Memastikan file ada sebelum melanjutkan. Jika tidak ada, program akan exit.

```python
cards = retrieve_cards_from_file()
```
**Baris 54**: Memuat semua kartu dari file ke dalam variabel `cards`.

```python
print("Kamu memiliki " + str(len(cards)) + " kartu untuk ditebak")
```
**Baris 55**: Memberi tahu pengguna berapa banyak kartu yang akan dipelajari.

```python
input("Siap? Tekan ENTER untuk memulai")
```
**Baris 56**: Menunggu pengguna menekan ENTER sebelum memulai timer. Ini memberi waktu untuk membaca jumlah kartu.

```python
time_begin = time.time()
```
**Baris 57**: Mencatat waktu mulai dalam detik sejak epoch (1 Januari 1970).

```python
guess_cards(cards)
```
**Baris 58**: Memulai proses belajar. Fungsi ini akan berjalan sampai semua kartu ditebak dengan benar.

```python
time_end = time.time()
```
**Baris 59**: Mencatat waktu selesai.

```python
duration = int(time_end - time_begin)
```
**Baris 60**: Menghitung durasi dalam detik dan mengkonversi ke integer (membulatkan ke bawah).

```python
print("Kamu berhasil menebak seluruh kartu dalam " + str(duration) + " detik.")
```
**Baris 61**: Mencetak pesan sukses dengan durasi yang dibutuhkan.

```python
print("Program selesai!")
```
**Baris 62**: Mencetak pesan bahwa program telah selesai.

---

## Ringkasan Hubungan Kedua File

### Format Data yang Digunakan

Kedua file menggunakan format data yang sama:
- **Struktur**: List of tuples
- **Format tuple**: `(kata_inggris, kata_indonesia)`
- **Contoh**: `[("hello", "halo"), ("world", "dunia")]`

### File yang Dibagikan

Kedua file membaca dan menulis ke file yang sama: **`flash_cards.txt`**

### Alur Data

1. **Pembuatan Kartu** (`add_flash_cards.py`):
   - User memasukkan kata Inggris
   - Program menerjemahkan ke bahasa Indonesia
   - Kartu disimpan ke `flash_cards.txt`

2. **Pembelajaran** (`study_flash_cards.py`):
   - Program membaca kartu dari `flash_cards.txt`
   - User menebak terjemahan
   - Kartu yang benar dihapus dari list (hanya di memori, tidak mengubah file)

### Fungsi yang Sama

Kedua file memiliki fungsi `retrieve_cards_from_file()` yang identik, yang menunjukkan bahwa mereka bekerja dengan format data yang sama.

### Perbedaan Utama

| Aspek | add_flash_cards.py | study_flash_cards.py |
|-------|-------------------|---------------------|
| **Tujuan** | Membuat kartu baru | Mempelajari kartu |
| **Mengubah file** | Ya (menulis) | Tidak (hanya membaca) |
| **Async** | Ya (untuk translate) | Tidak |
| **Random** | Tidak | Ya (urutan acak) |
| **Timer** | Tidak | Ya (mengukur waktu) |
| **Validasi input** | y/n dan kata tidak kosong | Input tidak kosong |

---

## Tips Penggunaan

1. Jalankan `add_flash_cards.py` terlebih dahulu untuk membuat kartu sebelum belajar
2. File `flash_cards.txt` akan dibuat otomatis saat pertama kali menyimpan kartu
3. Kartu yang salah ditebak akan muncul lagi sampai ditebak dengan benar
4. Urutan kartu di `study_flash_cards.py` adalah acak
5. Waktu dihitung dari saat mulai sampai semua kartu benar