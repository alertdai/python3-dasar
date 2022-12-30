# Belajar Method Parameter

# print("Ini adalah parameter")

# Single Parameter
def say_hello(nama):
    print(f"Hello {nama}")
    print(type(nama))

say_hello("Alva")

# Parameters
def say_hello_2(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

firstname = "Alex"
lastname = "Varhoud"
say_hello_2(firstname, lastname)