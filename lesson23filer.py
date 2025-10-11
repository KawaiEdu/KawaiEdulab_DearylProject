def diskon(harga, persen):
    potongan = harga * persen /100
    return harga - potongan

def pajak(harga, persen):
    hitung_tambahan = harga * persen /100
    hitung_hasil = harga + hitung_tambahan
    return hitung_hasil

while True :
    print("/n1. diskon", "2. pajak 3.keluar")
    chochie = int(input("masukan pilihan mu"))

    if chochie == 1:
        harga = int(input("masukan harga: "))
        persen = int(input("masukan persen: "))
        hasil_diskon = diskon(harga, persen)
        print(f"diskon adalah {hasil_diskon}")
    elif chochie == 2:
        harga = int(input("masukan harga: "))
        persen = int(input("masukan persen: "))
        hasil_pajak = pajak(harga, persen)
        print(f"pajak adalah {hasil_pajak}")
    elif chochie == 3:
        print("terima kasih see the next time")
        break
    else :
        print("yo homie wrong")