selamat_ulang_tahun = int(input("berapa kali kamu mau ucapan selamat ulang tahun "))
ulang = 10

if selamat_ulang_tahun > ulang :
    print("kelebihan mohon pengertian")
else :
    hitung = 1
    while hitung <= selamat_ulang_tahun :
        print(f"selamat ulang tahun ke-{hitung}")
        hitung += 1