# OPERASI LOGIKA ATAU BOOLEAN
# not, or, and, xor

print('===NOT===')
a = True
b = not a
print('data a =',a)
print('------------ NOT')
print('data b =',b)

# OR (jika salah satu true, maka hasilnya adalah true)
print('===OR===')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

# AND (jika dua buah nilai true, maka hasil true)
print('===AND===')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR (akan true jika salah satu true, sisanya false)
print('===XOR===')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)




#TUGAS PRAKTIKUM 4
umur = int(input("Masukkan Umur="))

if umur >= 0 and umur <= 12:
    print("Anda terdeteksi masih Anak-anak")
elif umur >= 13 and umur <= 17:
    print("Anda dalam masa Remaja")
elif umur >= 18 and umur <= 59:
    print("Anda sudah Dewasa")
elif umur >= 60:
    print("Menjadi Lansia adalah kepastian")
else:
    print("Anda tidak dilahirkan ke dunia ini")
