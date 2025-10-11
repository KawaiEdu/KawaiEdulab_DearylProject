jadwal_kesaharian_dirumah_tidak_prioritas = []
jadwal_kesaharian_dirumah_prioritas = ["belajar", "makan", "rapihkan tas", "cuci piring"]
while True: 
    print("\nJadwal kesaharian dirumah:", jadwal_kesaharian_dirumah_tidak_prioritas)
    print("1. Tambah item")
    print("2. Hapus item")
    print("3. Copy")
    print("4. combine")
    print("5. keluar")
    choice = int(input("pilih opsi(1/2/3/4/5): "))

    if choice == 1:
      item = input("Masukan item yang ingin ditambahkan: ") # Output input memasukkan data
      jadwal_kesaharian_dirumah_tidak_prioritas.append(item)
    elif choice == 2:
      item = input("Masukan item yang ingin dihapus") # output input menghapus data
      if item in jadwal_kesaharian_dirumah_tidak_prioritas:
         jadwal_kesaharian_dirumah_tidak_prioritas.remove(item)
    elif choice == 3:
       item = jadwal_kesaharian_dirumah_tidak_prioritas.copy
       jadwal_kesaharian_dirumah_tidak_prioritas.append("gacha")
       print(item) # Output: ["gacha"]
    elif choice == 4:
       combine = jadwal_kesaharian_dirumah_prioritas + jadwal_kesaharian_dirumah_tidak_prioritas
       print(combine)
       jadwal_kesaharian_dirumah_tidak_prioritas.extend(jadwal_kesaharian_dirumah_prioritas)
       print(jadwal_kesaharian_dirumah_prioritas)
    elif choice == 5: 
       print("terimakasih telah menggunakan program ini")
       break
    else:
       print("pilihan anda salah")