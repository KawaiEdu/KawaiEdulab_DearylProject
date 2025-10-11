def diskon(harga, persen):
    potongan = harga * persen /100
    return harga - potongan

#contoh penggunaan:
print(diskon(100000, 20)) # output:80000.0