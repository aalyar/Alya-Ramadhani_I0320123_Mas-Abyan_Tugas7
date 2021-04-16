nama =  "halo nama aku Alya"

print(nama)
print("------------------>")
#mengubah kata dalam string
print(nama.replace("aku", "saya"))

print("------------------>")
#mengubah kalimat menjadi huruf kecil, huruf besar, dan huruf kapital
print(nama.lower())
print(nama.upper())
print(nama.capitalize())

print("------------------>")
#mengupdate nilai string
print("Update : ", nama[:19] + ' Ramadhani')

print("------------------>")
#menampilkan string pada posisi tengah dengan tambahan karakter tertentu
print(nama.center(22, '^'))
