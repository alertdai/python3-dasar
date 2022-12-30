# Belajar Elif

menu_pilihan = input("Silahkan pilih menu [1-3] : ")

word = "Anda memilih menu "
word_complete = f"Anda memilih menu {menu_pilihan}"

if menu_pilihan == "1":
    print(f"{word} {menu_pilihan}")
elif menu_pilihan == "2":
    print(word_complete)
elif menu_pilihan == "3":
    print("Anda memilih menu 3")
else:
    print("Menu yang anda pilih tidak ada")