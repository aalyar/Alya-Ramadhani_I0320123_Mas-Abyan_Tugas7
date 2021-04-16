a = 5
b = -12
c = 23.2
d = 2
e = 10.5

f = [2,5,6,9,12,15]

#mencari nilai minimum dan maksimum
print("Nilai minimum = ", min(a,b,c,d,e))
print("Nilai maksimum = ", max(a,b,c,d,e))

print("------------------------")
#menampilkan hasil pemangkatan
print("Hasil dari ", d, "pangkat", a, "yaitu", pow(d,a))

print("----------------------------------")
#menampilkan nilai ceil dan floor pada suatu bilangan
import math
print("Pembulatan ke bawah dari ", c, "yaitu ", math.floor(c))
print("Pembulatan ke bawah dari ", e, "yaitu ",math.floor(e))
print("------------------------------------------")
print("Pembulatan ke bawah dari ", c, "yaitu ", math.ceil(c))
print("Pembulatan ke bawah dari ", e, "yaitu ", math.ceil(e))

print("------------------------------------------")
#menampilkan fungsi choice dan randrange
import random
print("Nilai yang terpilih yaitu", random.choice(f))
