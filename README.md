# M2_Programming2_FileHandling

**Latihan 1 - Silahkan buat program yang berisi menu untuk membaca dan menuliskan text ke dalam suatu file txt.**
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
Kenapa disini saya menggunakan fungsi def yang rumit karena file yang saya tuju itu langsung ke data.txt bu, file sudah saya sediakan sebelumnya tanpa membuat program eksternal untuk create file baru untuk kita, cuman minusnya adalah kita tidak dapat menambahkan atau seleksi file langsung melalui program yang dijalankan, harus manual membuat file dan memanggilnya di program, ini adalah kode penting untuk mengakses file itu:
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





