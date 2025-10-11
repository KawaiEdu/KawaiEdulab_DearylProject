kamus_buah = {
    "apel": "buah berwarna merah",
    "jeruk": "buah berwarna oranye",
    "pisang": "buah berwarna kuning",
}

buah = input("Masukan nama buah: ")
if buah in kamus_buah:
    print(f"{buah}: {kamus_buah[buah]}")
else:
    print("Buah tidak ditemukan dalam kamus")