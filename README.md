## Translator (Flash Cards EN → ID)

Program sederhana untuk membuat kartu terjemahan (Inggris → Indonesia) dan memainkannya sebagai kuis tebak terjemahan.

### Struktur Utama
- `add_flash_cards.py`: menerjemahkan kata dan menyimpan kartu ke `flash_cards.txt`.
- `study_flash_cards.py`: membaca kartu dari file yang sama dan menjalankan kuis, menghitung durasi penyelesaian.

### Versi Python yang Disarankan
- Python: 3.12.x

Catatan: googletrans versi yang dipakai tidak kompatibel dengan Python 3.13/3.14 karena dependensi `httpx` lama. Gunakan Python 3.12 untuk menghindari error modul `cgi` yang dihapus pada versi baru.

### Dependencies
- googletrans==4.0.0rc1
- httpx==0.13.3
- httpcore==0.9.1

Disarankan membuat file `requirements.txt`:

```txt
googletrans==4.0.0rc1
httpx==0.13.3
httpcore==0.9.1
```

### Instalasi (Windows PowerShell, tanpa venv)
Pastikan Python 3.12 terpasang dan terdeteksi oleh Python Launcher.

```powershell
py -0p                # verifikasi daftar interpreter, pastikan ada 3.12
py -3.12 -m pip install --upgrade pip
py -3.12 -m pip install -r requirements.txt
```

Atau instal langsung tanpa `requirements.txt`:

```powershell
py -3.12 -m pip install "googletrans==4.0.0rc1" "httpx==0.13.3" "httpcore==0.9.1"
```

### Menjalankan Program

```powershell
py -3.12 add_flash_cards.py     # membuat & menyimpan kartu terjemahan
py -3.12 study_flash_cards.py   # kuis tebak terjemahan + hitung durasi
```

### Catatan Teknis
- Data kartu disimpan di `flash_cards.txt` sebagai representasi list Python (dibaca dengan `ast.literal_eval`).
- Pastikan menjalankan dengan Python 3.12 agar `googletrans==4.0.0rc1` dan `httpx==0.13.3` berjalan lancar.