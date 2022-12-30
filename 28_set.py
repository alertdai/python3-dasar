# Belajar Set

# Data yg bisa disimpan harus unique
# Tidak bisa mengakses data menggunakan index, harus menggunakan for loop

coba_set = {}
print("Inisialisasi")
nama = {"Eko", "Joko", "Eko", "Andi"}

print(nama)
print("=====================")
print("Menambahkan nama baru")
nama.add("Kurniawan")
nama.add("Kurniawan")
nama.add("Kurniawan")

for data in nama:
    print(data)

print("=====================")
print("Menghapus nama")
nama.remove("Eko")

for data in nama:
    print(data)