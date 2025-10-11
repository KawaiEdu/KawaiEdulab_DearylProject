while True:
    print("\nmenu: [1] sapa [2] hitung [0] keluar")
    choiche = input("pilih: ").strip()
    if not choiche:
        continue
    if choiche == "0":
        print("sampai jumpa")
        break
    elif choiche == "1":
        nama = input("Namamu: ").strip()
        if not nama:
            continue
        print("halo, ", nama +"!" )
    elif choiche == "2":
        n = int(input("masukan N : "))
        total = 0
        for i in range(1, n+1):
            total += i
            print("jumlah 1..", n, "=", total)
    else:
        print("pilihan tidak valid")