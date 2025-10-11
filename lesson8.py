nilai = int(input("Masukan nilai: "))

if nilai >= 90:
    print(f"{nilai} masuk grade A")
elif nilai >= 80:
    print(f"{nilai} masuk grade B")
elif nilai >= 70:
    print(f"{nilai} masuk grade C")
else :
    print(f"{nilai} masik grade F")