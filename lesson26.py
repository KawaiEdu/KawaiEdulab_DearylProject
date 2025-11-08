def hitung_mundur(n):
    if n == 0:            # base case
        print("Go!")
        return
    print(n)
    hitung_mundur(n-1)    # panggilan rekursif

hitung_mundur(5)