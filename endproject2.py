import os
import json

def tulisan_catatan (filename, data_buku):
    with open(filename, "w") as file:
        file.write(json.dumps(data_buku, indent=4))

def baca_catatan(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = file.read()
            if data :
                return json.loads(data)
            else:
                return[]
    else:
        return[]

def isibuku(filename):
    id_buku = input("masukkan id buku ")
    judul_buku = input("masukan judul buku ")
    tahun_buku = input("masukan tahun buku ")
    nama_penerbit = input("masukan nama penerbit buku ")

    isi_buku = {
        "id_buku":id_buku,
        "judul_buku":judul_buku,
        "tahun_buku":tahun_buku,
        "nama_penerbit":nama_penerbit
        }

    data_buku = baca_catatan(filename)
    data_buku.append(isi_buku)

    tulisan_catatan(filename, data_buku)
    print("buku berhasil ditambahkan")

def cari_buku(filename):
    id_buku = input("masukan id buku yang ingin di cari: ")
    data_buku = baca_catatan(filename)

    for buku in data_buku:
        if buku ["id_buku"]==id_buku:
            print(f"\nbuku di temukan:{buku}")
            return
        print("buku tidak di temukan ")

def tampilkan_buku(filename):
    data_buku = baca_catatan(filename)

    if data_buku:
        print("\ndaftar buku di perpustakaan")
        for buku in data_buku:
            print(f"{buku['id_buku']} - {buku['judul_buku']} oleh {buku['nama_penerbit']} ({buku['tahun_buku']})")

def main():
    filename = "data_buku.txt"

    while True:
        print("\nmenu perpustakaan")
        print("1.isi buku")
        print("2.cari buku")
        print("3.tampilkan buku")
        print("4.keluar")
        choiche = input("\npilih menu: ")

        if choiche == '1':
            isibuku(filename)
        elif choiche == '2':
            cari_buku(filename)
        elif choiche == '3':
            tampilkan_buku(filename)
        elif choiche == '4':
            print("\nthanks")
            break
        else:
            print("Error")
if __name__=="__main__":
    main()