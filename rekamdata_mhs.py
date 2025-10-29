import sys
import os

class Mahasiswa:
    def __init__(self):
        self.nim = 0
        self.nama = ""

dataSiswa = []  # gunakan satu nama variabel yang konsisten

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Menu Aplikasi Data Siswa Linked List Python")
    print("-------------------------------------------")
    print("1. Input data siswa")
    print("2. Tampilkan data siswa")
    print("3. Update data siswa")
    print("4. Hapus data siswa")
    print("5. Author")
    print("6. Keluar aplikasi")

    try:
        pilih = int(input("Masukkan pilihan anda: "))
    except ValueError:
        print("Input harus berupa angka!")
        input("Tekan Enter untuk kembali ke menu...")
        return menu()

    if pilih == 1:
        pilih1()
        menu()
    elif pilih == 2:
        tampil()
        input("Tekan Enter untuk kembali ke menu...")
        menu()
    elif pilih == 3:
        update()
        input("Tekan Enter untuk kembali ke menu...")
        menu()
    elif pilih == 4:
        hapus()
        input("Tekan Enter untuk kembali ke menu...")
        menu()
    elif pilih == 5:
        author()
        input("Tekan Enter untuk kembali ke menu...")
        menu()
    elif pilih == 6:
        sys.exit()
    else:
        print("Pilihan tidak valid!")
        menu()

def pilih1():
    ulang = 'Y'
    while ulang in('y','Y'):
        os.system('cls')
        siswaBaru = Mahasiswa()   # ← tambahkan baris ini!
        siswaBaru.nim = int(input("masukkan nim : "))
        siswaBaru.nama = input("masukkan nama siswa : ")
        dataSiswa.append(siswaBaru)
        ulang = input("apakah anda ingin mengulang (Y/ T) ?")


def tampil():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Data Mahasiswa")
    print("----------------------")
    if not dataSiswa:
        print("Belum ada data mahasiswa.")
    else:
        for data in dataSiswa:
            print(f"NIM  : {data.nim}")
            print(f"Nama : {data.nama}")
            print("----------------------")

def update():
    tampil()
    id_edit = int(input("Masukkan NIM yang akan diupdate: "))
    index_update = -1
    for i in range(len(dataSiswa)):
        if dataSiswa[i].nim == id_edit:
            index_update = i
            break
    if index_update > -1:
        print("Input data baru:")
        siswa = Mahasiswa()
        siswa.nim = int(input("Masukkan NIM baru: "))
        siswa.nama = input("Masukkan nama baru: ")
        dataSiswa[index_update] = siswa
        print("Data berhasil diupdate!")
    else:
        print("NIM tidak ditemukan!")

def hapus():
    tampil()
    id_hapus = int(input("Masukkan NIM yang akan dihapus: "))
    index_delete = -1
    for i in range(len(dataSiswa)):
        if dataSiswa[i].nim == id_hapus:
            index_delete = i
            break
    if index_delete > -1:
        del dataSiswa[index_delete]
        print("Data berhasil dihapus!")
    else:
        print("NIM tidak ditemukan!")

def author():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Author: Alvin Meko | 1234567890")
    print("Universitas Kristen Satya Wacana (UKSW) 2016")

menu()
