daftar_belanja = [] # ini adalah variabel jadwal kesaharian di rumah

while True:
    print("\nDaftar Belanja:",daftar_belanja)
    print("1. Tambah item")
    print("2. Hapus item")
    print("3. keluar")
    choice = int(input("pilih opsi(1/2/3): "))
    
    if choice == 1:
      item = input("Masukan item yang ingin ditambahkan: ")
      daftar_belanja.append(item)
    elif choice == 2:
      item = input("Masukan item yang ingin dihapus")
      if item in daftar_belanja:
         daftar_belanja.remove(item)
      else :
         "print("item 
    elif choice == 3:
       print("Terima kasih telah menggunakan program ini")
       break
    else:
       print("Pilihan tidak valid, coba lagi.")