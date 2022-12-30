# Belajar List

# Index dimulai dari 0

names = []
names.append("eko")
names.append("budi")
names.append("maman")

print(names[0])
print(names[1])
print(names[2])

print(f"Panjang list names ada : {len(names)}")

names.remove("budi")

print(names)
print(f"Panjang list names setelah dihapus ada : {len(names)}")