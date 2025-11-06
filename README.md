## Translator (Flash Cards EN → ID)

Program sederhana untuk membuat kartu terjemahan (Inggris → Indonesia) dan memainkannya sebagai kuis tebak terjemahan.

### Struktur Utama
- `add_flash_cards.py`: menerjemahkan kata dan menyimpan kartu ke `flash_cards.txt`.
- `study_flash_cards.py`: membaca kartu dari file yang sama dan menjalankan kuis, menghitung durasi penyelesaian.

### Versi Python yang Disarankan
- Python: 3.14.x

### Dependencies
- googletrans (versi terbaru)

Disarankan membuat file `requirements.txt`:

```txt
googletrans
```

### Instalasi (Windows PowerShell)
Pastikan Python 3.14 terpasang dan terdeteksi oleh Python Launcher.

```powershell
py -0p                # verifikasi daftar interpreter, pastikan ada 3.14
py -3.14 -m pip install --upgrade pip
py -3.14 -m pip install -r requirements.txt
```

Atau instal langsung tanpa `requirements.txt`:

```powershell
py -3.14 -m pip install googletrans
```

### Menjalankan Program

```powershell
py -3.14 add_flash_cards.py     # membuat & menyimpan kartu terjemahan
py -3.14 study_flash_cards.py   # kuis tebak terjemahan + hitung durasi
```

### Catatan Teknis
- Data kartu disimpan di `flash_cards.txt` sebagai representasi list Python (dibaca dengan `ast.literal_eval`).
- Program menggunakan googletrans terbaru yang kompatibel dengan Python 3.14.