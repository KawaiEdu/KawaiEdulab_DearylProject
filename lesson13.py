
hari_libur = ("sabtu", "minggu")
hari = input("masukan hari: ")
while True:
    print("\nhari libur:", hari_libur)
    print("1. cek hari ini libur atau sekolah atau kerja")
    print("2. keluar")
    choice = int(input("pilih opsi 1/2 "))
    if choice == 1:

        if hari in hari_libur:
            print(f"hari ini hari libur")

        else:
            print(f"hari ini hari sekolah atau kerja")
    elif choice == 2:
        break