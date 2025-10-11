while True:
    print("\n====Program Kalkulator====")

    print("-----Menu kalkulator")
    x = float(input("masukan angka pertama "))
    y = float(input("masukan angka ke dua "))

    tambah = lambda x, y: x + y
    kurang = lambda x, y: x - y
    kali = lambda x, y: x * y 
    bagi = lambda x, y: x / y

    print("\n1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    choice = int(input("masukan pilihan kamu "))

    if choice == 1:
        print(f"\nHasil pertambahan : ",{tambah(x, y)})
    elif choice == 2:
        print(f"\nHasil pengurangan : ",{kurang(x, y)})
    elif choice == 3:
        print(f"\nHasil perkalian : ",{kali(x, y)})
    elif choice == 4:
        print(f"\nHasil pembagian : ",{bagi(x, y)})
    else :
        print("Pilihan salah")