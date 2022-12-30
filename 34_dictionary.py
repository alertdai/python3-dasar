# Belajar Tipe Data Dictionary

customer = {"Nama":"Alva","Umur":30,"Alamat":"Bogor"}

print(customer["Nama"])
umur = customer["Umur"]
print(umur)
print("=================================")

# Cara pertama mengakses dict dengan for untuk menampilkan nama key saja
for data in customer:
    print(data)
print("=================================")

# Cara kedua mengakses dict untuk mendapatkan isi dari key
for key in customer:
    value = customer[key]
    print(f"{key} : {value}")
print("=================================")

# Cara ketiga mengakses dict, mendapatkan isi dari key secara simple
print(customer.items()) #Bentuk dari .items() merupkana list di dalam tuple
for item in customer.items():
    print(f"{item[0]} : {item[1]}")
print("=================================")

# Cara ketiga mengakses dict, mendapatkan isi dari key secara dengan return value
for key, value in customer.items():
    print(f"{key} : {value}")
print("=================================")

# Menambahkan data customer
customer["Pekerjaan"] = "QA"
print(customer)
print("=================================")

# Mengedit data customer
customer["Umur"] = 24
print(customer)
print("=================================")

# Menghapus data customer
del customer["Alamat"]
print(customer)
print("=================================")