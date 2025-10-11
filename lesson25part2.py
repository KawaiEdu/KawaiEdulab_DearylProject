angka = [0, -2, 4, 7, -1, 9, 12]
target = 9

for a in angka:
    if a < 0:
        continue
    if a == target:
        print("ketemu:", a)
        break
    print("cek:", a)