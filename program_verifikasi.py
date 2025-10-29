# program_verifikasi.py

data = input("Masukkan Umur Kamu: ")

# Coba ubah ke integer terlebih dahulu
try:
    angka = int(data)
    print(f"Data ini adalah angka integer. Angka = {angka}")
except ValueError:
    # Kalau tidak bisa jadi integer, coba ubah ke float
    try:
        angka = float(data)
        print(f"Data ini adalah data float. Angka = {angka}")
    except ValueError:
        # Kalau keduanya gagal, berarti itu string atau tipe lain
        print(f"Data yang anda inputkan adalah tipe string {data}")