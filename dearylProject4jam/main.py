# main.py
from rec import faktorial, fib, pangkat
from utils import to_int, menu

while True :
    menu ()
    choiche = input("pilih ").strip()
    if choiche == "0" :
        print(" bye"); break
    if choiche not in {"1", "2", "3"}:
        print("not valid"); continue

    a = to_int(input("masukan n /angka-1:"))
    if a is None: 
        print("harus angka"); continue

    if choiche == "1" :
        print("hasil:", faktorial(a))
    elif choiche == "2" :
        print("hasil:", fib(a))
    elif choiche == "3":
        b = to_int(input("Masukkan angka-2 (pangkat): "))
        if b is None: print("Harus angka!"); continue
        print("Hasil:", pangkat(a, b))