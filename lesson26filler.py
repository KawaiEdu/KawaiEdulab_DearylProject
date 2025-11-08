import sys
import time
from functools import lru_cache

def menu():
    print("\n===PROGRAM UHHH NACHO ....SOMETHING PYTHON===")
    print("1.rekursif normal (fibbonaci)")
    print("2. deep rekursif (nested list sum)")
    print("3.memoization (fibbonaci omptimized)")
    print("4.keluar")
    choiche =input("mau mana(1-4):")
    return choiche

def fibbonaci_rekursif(n):
    if n <= 1:
        return n
    return fibbonaci_rekursif(n-1) + fibbonaci_rekursif(n-2)

def deep_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total +=deep_sum(item)
        else :
            total += item
            return total
        
@lru_cache(maxsize=None)
def fibbonaci_memoization(n):
    if n <= 1:
        return n 
    return fibbonaci_memoization(n-1) + fibbonaci_memoization(n-2)

def main():
    while True:
        choiche = menu()
        if choiche == '1':
            n = int(input("masukan nilai fibbonaci:"))
            start = time.time()
            result = fibbonaci_rekursif(n)
            end = time.time()
            print(f"hasil:{result}(waktu:{end - start:4f}detik)")
        elif choiche == '2':
            nested = eval(input("masukan list bersarang contoh : [1,[2,[3,4]],5]:"))
            result = deep_sum(nested)
            print(f"total penjumlahan:{result}")
        elif choiche == '3':
            n = int(input("masukan niali n untuk fibbonaci(memoization):"))
            start = time.time()
            result = fibbonaci_memoization(n)
            end = time.time()
            print(f"hasil:{result}(waktu:{end - start:4f}detik)")
        elif choiche == '4':
            print("thanks")
            sys.exit()
        else:
            print("wrong")

if __name__=="__main__":
    main()