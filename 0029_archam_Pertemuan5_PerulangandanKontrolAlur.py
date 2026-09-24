#PROGRAM 5.1 FOR
# perulangan (loop

angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

#for kondisi
#aksi

#dengan list
angka2 = [0,1,2,3,4] #ini adalah list
print(angka2)

for i in angka2:
    print(f"i sekarang => {i}") #print(f) -> kombinasi text dan variabel
print("akhiri dari program\n")

#dengan range
angka3 = range(5)

for i in angka3:
    print(f"i sekarang => {i}")
print("akhiri dari program\n")

angka4 = range(1,10)
for i in angka4:
    print(f"i sekarang => {i}")
    #print("saya keren")
print("akhiri dari program\n")

#menggunakan string
data_str = "saya ganteng abiies"

for huruf in data_str:
    print(huruf)
print("akhiri dari program\n")




#PROGRAM 5.2 WHILE LOOP
# while loop
#while kondisi:
# aksi ini
# aksi itu
print("===contoh 1===\n")
      
angka = 10
while angka > 5:
    print("ipin lari ipin!!!")
print("===contoh 2===\n")

angka = 0
print(f"angka sekarang → {angka}")

while angka < 5:
    angka += 1
    #angka = angka + 1
    print(f"angka sekarang → {angka}")
    print("ipin lari ipin")

print("program berakhir, ipin sudah jauh")




#PROGRAM 5.3 Continue and Pass

# continue, pass, break
#pass → dia berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0
while angka < 5:
    angka = angka + 1
    if(angka == 3):
        pass # ini tidak akan dieksekusi
    print(angka)

#continue
angka = 0
print(f"angka sekarang → {angka}")
while angka < 5:
    angka = angka + 1
    print(f"angka sekarang → {angka}") # aksi 1
    if(angka == 3):
        print("nice")
        continue # akan membuat loop meloncat ke step selanjutnya
    print("whasssup") # aksi 2
print("Pinish")




#PROGRAM 5.4 Break
#Break

angka = 0
print (f"angka sekarang => {angka}")

while angka < 5:
    angka = angka +1
    print (f"angka sekarang => {angka}") #aksi 1

    if (angka == 3):
        print("nice")
        break
    print("whassup") #aksi 2

print("cukup mas")





#PROGRAM 5.5 Latihan Perulangan

# 1. Menggunakan for
sisi = 4
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

# 2. Menggunakan while
sisi = 4
count = 1
while True:
    print("*" * count)
    count += 1
    if count > sisi:
        break





#TUGAS PRAKTIKUM PERTEMUAN 5

# Soal 1
# Program Menampilkan Bilangan Ganjil dan Genap (1 - 50)

print("Bilangan Ganjil")

for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")

print("\nBilangan Genap")

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()

#Soal 2
#Program Menampilkam Semua Bilangan Prima (1 - 100)

print("Bilangan Prima (1 - 100)")

for angka in range(2, 101):
    is_prima = True
    
    # Memeriksa pembagi dari 2 hingga angka - 1
    for i in range(2, angka):
        if angka % i == 0:
            is_prima = False
            break  # Menghentikan pengecekan jika ditemukan pembagi lain
            
    if is_prima:
        print(angka, end=" ")
print()
