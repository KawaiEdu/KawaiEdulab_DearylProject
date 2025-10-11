kelas ={
    "kelas A": ["andi", "budi"],
    "kelas B": ["citra", "dedi"]
}

for nama_kelas, siswa in kelas.items():
    print(nama_kelas + ":")
    for s in siswa:
        print("-" + s)
    print()