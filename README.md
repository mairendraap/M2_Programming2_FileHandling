# M2_Programming2_FileHandling

## Latihan 1 - Silahkan buat program yang berisi menu untuk membaca dan menuliskan text ke dalam suatu file txt.
```python
import os

nama_file = "data.txt"
f_awal = open(nama_file, "a")
f_awal.close() 

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
```
Kenapa disini saya menggunakan fungsi def yang sangat simple ini karena file yang saya tuju itu langsung ke data.txt bu, file sudah saya sediakan sebelumnya tanpa membuat program eksternal untuk create file baru untuk kita, cuman minusnya adalah kita tidak dapat menambahkan atau seleksi file langsung melalui program yang dijalankan, harus manual membuat file dan memanggilnya di program, ini adalah kode penting untuk mengakses file itu (saya malas bertemu if atau elif apalagi kalau bertumpuk itu mumet bu:
```python
nama_file = "data.txt"
f_awal = open(nama_file, "a")
f_awal.close()
```
Mungkin bu lely bertanya, kenapa saya menggunakan a di open data tersebut. Karena saya tidak mau file yang sudah ada di data.txt itu tertimpa dengan file yang baru, jadi saya sesuaikan dengan menggunakan Mode Append. Kalau untuk yang w dan r itu sudah sangat basic yakni r untuk read dan w untuk write, ykwim (you know what i mean) hehe.

Satu lagi, saya menggunakan:
```python
aksi.get(pilihan, lambda: print("Pilihan tidak valid"))()
```
untuk menggantikan fungsi if atau elif karena saya mumet bu kalau pakai itu, apalagi kalau bertumpuk, jadi saya akalin menggunakan fungsi 'def' saya agar jelas maksud dan terorganisir disana.

**Output:**
<img width="1491" height="438" alt="image" src="https://github.com/user-attachments/assets/5b8bc3c3-8564-4ca7-9835-de9a01e53d39" />

## Latihan 2 - Menambahkan Context Manager
Jujur sama saja dengan kode saya sebelumnya bu, cuman saya mengganti sedikit di bagian yang awalnya:
```python
nama_file = "data.txt"
f_awal = open(nama_file, "a")
f_awal.close()
```
Menjadi:
```python
with open(nama_file, "a") as f:
```
Cuman itu aja, karena sebelumnya memang saya membuat fungsi serupa tapi kalau di context manager ini kan dibuat lebih simple kita tidak perlu pakai syntax open atau close lagi, dan lebih hemat memori.

Ini kode full nya:
```python
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
```
saya tambahkan 'pass' disana agar dia mengecek apakah file 'data.txt' itu sudah dibuat atau belum.

## Latihan 3 - Nama Unik/Unique Name/Daftar Nama itulah pokoknya
```python
import os

def simpan_nama_unik():
    nama_file = "data.txt"
    
    while True:
        nama_input = input("masukkan nama: ").strip()
        
        daftar_nama = []
        if os.path.exists(nama_file):
            with open(nama_file, "r") as f:
                daftar_nama = [line.strip() for line in f.readlines()]
        
        if nama_input in daftar_nama:
            print("nama sudah ada pada daftar")
        else:
            with open(nama_file, "a") as f:
                f.write(nama_input + "\n")
            print(f"Berhasil menambahkan {nama_input}")

        ulangi = input("ulangi masukkan nama (y/t)?").lower()
        if ulangi == 't':
            break

if __name__ == "__main__":
    simpan_nama_unik()
```
<img width="1288" height="128" alt="image" src="https://github.com/user-attachments/assets/a5d8448b-ff85-4294-9aaa-db7b16821ca2" />

ini sama saja seperti yang tadi waktu kita input nama di awal dan di save ke 'data.txt' tapi bedanya disini kita tanyakan ulang ke user apakah ingin menambahkan nama lagi dan jika 'true' dia dapat menambahkan nama, apabila nama yang di masukkan sama persis 'capital case' nya juga sistem akan merespon bahwa nama tersebut telah ada di file 'data.txt'. Ini sebenernya logikanya mudah saja, dimana kita hanya perlu read kembali data yang ada sebelum ke write jadi di fungsi if disana kita loop kesana, agar sistem mendeteksii terlebih dahulu apakah nama itu sudah ada di 'data.txt' atau belum.

## Latihan 4 - memfasilitasi user untuk membuat file txt baru pada working directory. 
```python
import os

def buat_file_baru():
    while True:
        nama_file = input("masukkan nama file: ")
        if not nama_file.endswith(".txt"):
            nama_file += ".txt"
            
        files_in_dir = os.listdir()
        
        if nama_file in files_in_dir:
            print("file sudah ada pada direktori tersebut")
            ulangi = input("ulangi membuat file baru (y/t)?").lower()
            if ulangi == 't':
                break
        else:
            with open(nama_file, "w") as f:
                pass 
            print(f"{nama_file} berhasil dibuat")
            ulangi = input("ulangi membuat file baru (y/t)?").lower()
            if ulangi == 't':
                break


if __name__ == "__main__":
    buat_file_baru()
```
<img width="1288" height="178" alt="image" src="https://github.com/user-attachments/assets/7fb3a672-5508-425b-8d77-1f7cb7fb9fb1" />
Fungsi ini sangat mirip dengan sebelumnya, namun ini kita merubah sebuah file. Saya mau jelasin satu satu untuk yang awal itu pastinya cek dulu apakah ada file dengan nama tersebut output terminal saya check terlebih dahulu dengan input 'data.txt' yang sebelumnya memang sudah ada di directory, disini saya sengaja membuat opsi menjadi lower agar orang membaca dengan teliti, jadi nanti kalau ada yang input menggunakan Y capital tidak akan merespon karena saya set ke lower saja. Dan setelahnya saya coba menggunakan ekstensi '.txt' karena di program saya sudah input filename end with '.txt', ternyata program paham kalau itu sebuah ekstensi file, dan selanjutnya dataherdan saja dan auto ada ekstensi '.txt'.

Sekain praktikum saya, terima kasih.





