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