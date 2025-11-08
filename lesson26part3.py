def faktorial(n):
    if n <= 1:  return n
    return n * faktorial(n-1)

def jumlah(n):
    if n == 0: return 0
    return n + jumlah(n-1)

def fib(n):
    if n <= 1: return n 
    return fib(n-1) + fib(n-2)

while True:
    print("\\n[1]faktorial [2]jumlah [3]fibonaci [0]keluar")
    choiche = input("mau mana: ")
    if choiche == "0": break
    if choiche == "1":
        n = int(input("n: "))
        print("hasil : ", faktorial(n))
    elif choiche == "2":
        n = int(input("n: "))
        print("hasil : ", jumlah(n))
    elif choiche == "3":
        n = int(input("n: "))
        print("hasil : ", fib(n))