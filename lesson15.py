daftar_belanja = set()

while True:
    belanja_kebutuhan = input("masukan item belanja yang ingin ditambahkan ")
    if belanja_kebutuhan.lower() == "selesai" :
        print("keluar dari program")
        break
    daftar_belanja.add(belanja_kebutuhan)
print("daftar belanja anda")
for i in daftar_belanja :
    print(f"-{i}")