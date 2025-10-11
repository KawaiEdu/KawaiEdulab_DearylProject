buah_favorit_1 = {"apel","jeruk","pisang"}
buah_favorit_2 = {"jeruk","mangga","pisang"}

while True:
    print("1. difference \n2. union \n3. intersection \n4. keluar")
    choiche = int(input("masukan pilihan :"))
    if choiche == 1 :
        beda1 = buah_favorit_1.difference(buah_favorit_2)
        beda2 = buah_favorit_2.difference(buah_favorit_1)
        print("Buah yang hanya disukai orang pertama:", beda1)
        print("Buah yang hanya disukai orang kedua:", beda2)
    elif choiche == 2 :
        semua_buah = buah_favorit_1.union(buah_favorit_2)
        print(semua_buah)
    elif choiche == 3 :
        sama = buah_favorit_1.intersection(buah_favorit_2)
        print("Buah yang sama disukai:", sama)
    elif choiche == 4 :
        print("thanks")
        break
    else :
        ("false")