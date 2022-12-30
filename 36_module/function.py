# Belajar Module

def say_nama(nama):
    return f"Halo namaku {nama}"

def say_umur(umur):
    return f"Umurku = {umur}"

def total(*list_angka):
    hasil = 0
    for angka in list_angka:
        hasil += angka
    return hasil