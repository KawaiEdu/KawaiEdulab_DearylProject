buah = ["apel", "jeruk", "semangka"]                        # Ini adalah variabel buah
daging = ["daging sapi", "daging kambing", "daging ayam"]   # Ini adalah variabel daging
combine = buah + daging 

print(combine) # Output: ["apel", "jeruk", "semangka", "daging sapi", "daging kambing", "daging ayam"]
buah.extend(daging)
print(buah) # Output: ["apel", "jeruk", "semangka", "daging sapi", "daging kambing", "daging ayam"]

var_new = daging.copy()
var_new.append("daging kalkun")
print(var_new) # Output: ["daging sapi","daging kambing", "daging ayam", "daging kalkun"]