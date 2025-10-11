def kalkulator():
    try:
        angka1 = float(input("masukan angka pertama ")) 
        angka2 = float(input("masukan angka ke dua "))
        operasi = input("masukan operasi (+, -, *, /) ")

        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == "/":
            hasil = angka1 / angka2
        else :
            print("operasi tidak valid")

        return print(f"hasil : {hasil}")
    except ZeroDivisionError:
        print("tidak bisa di bagi nol")
    except ValueError:
        print("input harus angka")
    
while True:
    print("\n kalkulator sederhana")
    kalkulator()
    again = input("apakah anda ingin menghitung lagi ")
    if again.lower() !="ya":
        print("terimakasih sampai jumpa lagi")
        break