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
