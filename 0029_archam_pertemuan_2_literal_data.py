# Deklarasi variabel
nama = "Muhammad Archam Ikhsanudin"
umur = 18
berat = 65.1

# Menampilkan output
print("Nama :", nama)
print("Umur :", umur, "tahun")
print("Berat:", berat, "Kg")





# Tipe data yang akan diubah
angka_string = "123"
angka_float = 45.67
angka_integer = 89

# Konversi string ke integer
angka_string = "123"
angka_integer = int(angka_string)
print("Konversi string ke integer:", angka_integer, "type:", type(angka_integer))

# Konversi float ke integer
angka_float = 45.67
angka_integer = int(angka_float)
print("Konversi float ke integer:", angka_integer, "type:", type(angka_integer))

# Konversi integer ke float
angka_integer = 89
angka_float = float(angka_integer)
print("Konversi integer ke float:", angka_float, "type:", type(angka_float))

# Konversi integer ke string
angka_integer = 89
angka_string = str(angka_integer)
print("Konversi integer ke string:", angka_string, "type:", type(angka_string))





# Program Input Data Diri
# Meminta input usia (integer)
usia = int(input("Masukkan usia: 18"))

# Meminta input tinggi badan (float)
tinggi = float(input("Masukkan tinggi badan: 185.0"))

# Meminta input nama (string)
nama = input("Masukkan nama: Muhammad Archam Ikhsanudin")

# Menampilkan data hasil input
print("Nama        :", nama, ", type =", type(nama))
print("Usia        :", usia, ", type =", type(usia))
print("Tinggi Badan:", tinggi, ", type =", type(tinggi))