# Belajar Return Value

'''
Method dibagi 2:
    1. Prosedur : Mengeksekusi data yang ada
    2. Function : Method yang mengembalikan nilai

Cara untuk mengembalikan nilai argument atau
mengembalikan 2 value menggunakan tuple ('contoh : return (args1, args2)')
'''

# Menggunakan return value, data yang dikembalikan oleh method, dapat kita simpan di variable

def jumlahkan(x, *list_angka):
    total = 0
    for i in list_angka:
        total = total + i
    return (x, list_angka, total)

x, list_angka, total = jumlahkan(20, 10, 10, 10)

print(f"Hasil return x = {x}")
print(f"Hasil return list_angka = {list_angka}")
print(f"Hasil return total = {total}")



