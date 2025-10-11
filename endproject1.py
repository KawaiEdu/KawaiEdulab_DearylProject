while True:
    print("\n====Program Konversi Suhu====")

    print("-----MENU KONVERSI SUHU-----")

    Celcius = float(input("\nmasukan suhu dalam celcius "))
    Reamur = 4/5 * Celcius
    Fahrenheit = (Celcius * 9/5) + 32
    Kelvin = Celcius + 273.15

    print("\n1. Celcius")
    print("2. Reamur")
    print("3. fahrenheit")
    print("4. kelvin")
    print("5. Keluar")
    choice = int(input("masukan pilihan kamu "))

    if choice == 1:
        print(f"\nSuhu Celcius : {Celcius}")
    elif choice == 2:
        print(f"\nsuhu Celcius : {Celcius} ke Reamur : {Reamur}")
    elif choice == 3:
        print(f"\nsuhu Celcius : {Celcius} ke Fahrenheit : {Fahrenheit}")
    elif choice == 4:
        print(f"\nsuhu Celcius : {Celcius} ke Kelvin : {Kelvin}")
    elif choice == 5:
        print("Program telah selesai")
        break
    else :
        print("Pilihan anda salah")