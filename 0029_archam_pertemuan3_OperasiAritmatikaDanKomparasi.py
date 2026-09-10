#PROGRAM 3.1 Menampilkan output dari operasi aritmatika sederhana
#operasi aritmatika

a = 10
b = 3

#operasi tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

#operasi kurang -
hasil = a - b
print(a, "-", b, "=", hasil)

#operasi kali *
hasil = a * b
print(a, "*", b, "=", hasil)

#operasi pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

#operasi eksponen/pangkat **
hasil = a ** b
print(a, "**", b, "=", hasil)

#operasi modulus/sisa bagi %
hasil = a % b
print(a, "%", b, "=", hasil)

#operasi floor division //
hasil = a // b
print(a, "//", b, "=", hasil)


#PROGRAM 3.2 Konversi clcius ke satuan lain

#program konversi celsius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celsius = float(input("Masukkan suhu dalam celsius: "))

celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")


#PROGRAM 3.3 Operasi komperasi

#operasi komperasi
#setiap hasil dari operasi komprasi adalah boolean
# < , > , <= , >= , == , != ,is, is not

a = 4
b = 2

# lebih besar dari >
print("=============== lebih besar dari (>)")
hasil = a > 3
print(a, '>', b, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# kurang dari <
print("=============== kurang dari (<)")
hasil = a < 3
print(a, '<', b, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih dari sama dengan >=
print("=============== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a, '>=', b, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a, '<=', b, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan (==)
print("=============== sama dengan (==)")
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# tidak sama dengan (!=)
print("=============== sama dengan (!=)")
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)



#TUGAS PERTEMUAN 3

panjang = 12
lebar = 5
tinggi = 8

luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
volume = panjang * lebar * tinggi
keliling = 4 * (panjang + lebar + tinggi)

print("Luas Persegi Panjang adalah", luas)
print("Volume Balok adalah", volume)
print("Keliling Persegi Panjang adalah", keliling)

hasil = luas > 50
print("Apakah luas bangunan tersebut lebih luas dari 50?", hasil)

hasil = volume == 480
print("Apakah volume tersebut bernilai 480?", hasil)