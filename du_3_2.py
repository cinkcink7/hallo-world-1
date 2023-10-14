
# du_X_Y.py

# Ú 3.2: Hledáme mezeru
# Úkol:
# Ze standarního vstupu načtěte řetězec. Vypište první pozici mezery v tomto řetězci a
# tři znaky, které za ní následují. (Můžete předpokládat, že zadaný řetězec bude vždy
# obsahovat aspoň jednu mezeru.)
# Vzorový vstup:
# Zítra bude krásné počasí.

retezec = input("Zadej retezec: \n")
index_start = retezec.index(" ")
sub_retezec = retezec[index_start :index_start + 4]
print(f"{index_start } {sub_retezec}")

