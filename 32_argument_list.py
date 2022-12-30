# Belajar Argument List

# Untuk argument list tambahkan "*" di depan variabel
# dan jika ingin menambahkan argument biasa, maka argument list harus ditaruk di paling belakang

def jumlahkan(x, *list_angka):
    total = 0
    for i in list_angka:
        total = total + i
    print(f"Total penjumlahan list angka = {total}")

jumlahkan(20, 10, 10, 10)