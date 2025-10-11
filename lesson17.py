def tulis_catatan():
    catatan = input("masukan catatan anda: ")
    with open("catatan.txt","a") as file:
        file.write(catatan + "\n")
        print("catatan berhasil di simpan ")   

def baca_catatan():
    try:
        with open("catatan.txt", "r") as file:
            print("\n catatan harian anda:")
            print(file.read())
    except FileNotFoundError:
        print("belum ada catatan tersimpan.")
    
while True:
    print("\nPilih menu:")
    print("1. Tulis Catatan")
    print("2. Baca Catatan")
    print("3. Keluar")
    choiche = input("Masukkan pilihan (1/2/3): ")

    if choiche == "1":
        tulis_catatan()
    elif choiche == "2":
        baca_catatan()
    elif choiche == "3":
        print("thanks good bye")
        break
    else :
        print("not found")