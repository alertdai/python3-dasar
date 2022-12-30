# Belajar Default Argument Value

def pemisah():
    print("======================")

# Single Parameter
def say_hello(nama="Kosong"):
    print(f"Hello {nama}")

say_hello("Alva")
say_hello()
pemisah()
# 2 Parameters
# Jika memakai lebih dari 1 parameter, maka hanya bisa ditambahkan pada parameter terakhir
def say_hello_2(first_name, last_name=""):
    print(f"Hello {first_name} - {last_name}")

firstname = "Alex"
lastname = "Varhoud"
say_hello_2(firstname, lastname)
say_hello_2(last_name="Orang", first_name="Nama")
pemisah()
# 3 Parameters
# Jika memakai lebih dari 1 parameter, maka hanya bisa ditambahkan pada parameter terakhir
def say_hello_3(first_name, last_name, umur="-"):
    print(f"Hello {first_name} {last_name}, Umur anda {umur} tahun")

firstname = "Aldo"
lastname = "Trapani"
umur = 27
say_hello_3(firstname, lastname, umur)
say_hello_3("Kang", "Maman")