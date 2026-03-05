import os

nama_file = "data.txt"
with open(nama_file, "a") as f:
    pass 

def menu_tulis():
    teks = input("Masukkan inputan:")
    f = open(nama_file, "w")
    f.write(teks)
    f.close()
    print("Data sudah diinput")

def menu_baca():
    f = open(nama_file, "r")
    print("\nIsi data.txt:")
    print(f.read())
    f.close()

def menu_lihat_daftar():
    print("\nDaftar file di direktori:", os.listdir())

print(f"File Handling ({nama_file})")
print("1. Tulis ke data.txt")
print("2. Baca data.txt")
print("3. Lihat Daftar File")

pilihan = input("Pilih menu (1/2/3): ")

aksi = {
    "1": menu_tulis,
    "2": menu_baca,
    "3": menu_lihat_daftar
}

aksi.get(pilihan, lambda: print("Pilihan tidak valid"))()