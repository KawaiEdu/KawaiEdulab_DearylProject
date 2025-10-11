def luas_persegi(sisi):
    return sisi * sisi

def luas_lingkaran(jari):
    return 3.14 * jari * jari

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def volume_kubus(sisi):
    return sisi * sisi * sisi

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def volume_tabung(Jari, tinggi):
    return 3.14 * Jari * tinggi  

while True:
    print("\n1. Luas persegi")
    print("2. Luas lingkaran")
    print("3. Luas persegi panjang")
    print("4. Volume kubus")
    print("5. Volume balok")
    print("6. Volume tabung")
    choice = int(input("masukan pilihan kamu "))

    if choice == 1:
        print("Menu Luas Persegi")
        sisi = int(input("Masukkan Sisi Persegi: "))
        hasil_luas = luas_persegi(sisi)
        print(f"Luas Persegi Adalah {hasil_luas}")
    elif choice == 2:
        print("Menu luas Lingkaran")
        jari = float(input("Masukan Jari-Jari Lingkaran: "))
        hasil_luas = luas_lingkaran(jari)
        print(f"Luas Lingkaran Adalah {hasil_luas}")
    elif choice == 3: 
        print("Menu Luas Persegi Panjang")
        Panjang = int(input("Masukan Panjang Persegi Panjang: "))
        Lebar = int(input("Masukan Lebar persegi panjang: "))
        hasil_luas = luas_persegi_panjang(Panjang, Lebar)
        print(f"Luas Persegi panjang Adalah {hasil_luas}")
    elif choice == 4:
        print("Menu Volume kubus")
        sisi = int(input("Masukan Sisi kubus: "))
        hasil_volume = volume_kubus(sisi)
        print(f"volume kubus Adalah {hasil_volume}")
    elif choice == 5:
        print("Menu volume Balok")
        Panjang = int(input("Masukan panjang: "))
        Lebar = int(input("Masukan Lebar: "))
        tinggi = int(input("Masukan Tinggi: "))
        hasil_volume = volume_balok(Panjang, Lebar, tinggi)
        print(f"Volume balok Adalah {hasil_volume}")
    elif choice == 6:
        print("Menu volume Tabung")
        jari = int(input("Masukan Jari-jari: "))
        tinggi = int(input("Masukan Tinggi: "))
        hasil_volume = volume_tabung(jari, tinggi)
        print(f"Volume balok Adalah")
    else :
        print("Pilihan anda salah")