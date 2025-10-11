buah_favorit_1 = {"apel","jeruk","pisang"}
buah_favorit_2 = {"jeruk","mangga","pisang"}

# Buah yang sama
sama = buah_favorit_1.intersection(buah_favorit_2)
print("Buah yang sama disukai:", sama)

# Buah yang berbeda
beda1 = buah_favorit_1.difference(buah_favorit_2)
beda2 = buah_favorit_2.difference(buah_favorit_1)
print("Buah yang hanya disukai orang pertama:", beda1)
print("Buah yang hanya disukai orang kedua:", beda2)