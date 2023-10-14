
# du_X_Y.py

# DÚ 3.4: DNA
# Sekvence DNA se skládá ze čtyř typů nukleových bazí (A, C, G, T). Absolutní četnost
# báze vyjádřuje, kolikrát se vyskytuje daná báze v sekvenci.
# Úkol:
# Ze standardního vstupu načtěte sekvenci DNA. Na výstup vypište absolutní četnosti
# jednotlivých bazí.
# Vzorový vstup 1:   Vzorový vstup 2:  
# ACGTTTTGAG AAAACCCCTTTTTTTTTT
# Vzorový výstup 1:   Vzorový výstup 2:  
# A: 2 A: 4
# C: 1 C: 4
# G: 3 G: 0
# T: 4 T: 10

sekvence = input("Zadej retezec DNA: \n")

a = sekvence.count("A")
t = sekvence.count("T")
c = sekvence.count("C")
g = sekvence.count("G")

# print(f"A : {a} C : {c} G : {g} T : {t}")
print(f"A : {a}\nC : {c}\nG : {g}\nT : {t}")

