# Uvod od Pythonu MUNI Domaci ukol 3 Sadovsky Martin

print("hallo world")

###############################################################################3
# Cvičení 3.1: Je to slovo?
# Úkol:
# Napište kód, který načte řetězec ze standarního vstupu pomocí funkce input. Poté
# rozhodne, jestli načtený řetězec je jedno slovo (tj. skládá se pouze z písmen). Pokud
# ano, vypíše True, v opačném případě False. Pro výpis použijte funkci print.
# Vzorový vstup 1:   Vzorový vstup 2:   Vzorový vstup 3:  
# Alohomora Wingardium leviosa 9
# Vzorový výstup 1:   Vzorový výstup 2:   Vzorový výstup 3: 


""" slovo = "martin"

# "a" in slovo
# print(" " in slovo)

slovo = input("Zde napis cokoliv a ja ti reknu zadali je to slovo : \n")
def kontrola_stringu(slovo):
    if " "in slovo:
        return False
    elif "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in slovo:
        return False
    else:
        return True


print(kontrola_stringu(slovo)) """

#########################################################################################

# Cvičení 3.2: Násobička
# Úkol:
# Napište kód, který ze standarního vstupu načte dvě celá čísla a na výstup vypíše jejich
# součin.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 2 3 -111 -6
# Vzorový výstup 1:   Vzorový výstup 2:  
# 6 666

""" a = int(input("Napis prvni cislo: \n"))
b = int(input("Napis druhe cislo: \n"))
soucin = a * b
print(soucin) """

##########################################################################################

# Cvičení 3.3: Palindrom?
# Palindrom je slovo nebo věta, která má stejné pořadí písmen zleva doprava a zprava
# doleva. Nezáleží při tom na velikosti písmen a na výskytu mezer.
# Úkol:
# Ze vstupu načtěte řetězec a rozhodněte, zda je to palindrom. (Můžete spoléhat, že
# vstup nebude obsahovat jiné znaky kromě písmen a mezer.)
# Vzorový vstup 1:   Vzorový vstup 2:   Vzorový vstup 3:  
# Jelenovi pivo nelej Jelen chce pivo Anna
# Vzorový výstup 1:   Vzorový výstup 2:   Vzorový výstup 3:  
# True False True

# palindrom = "Jelenovi pivo nelej"
# bez_mezery = palindrom.replace(" ", "")
# bez_mezery_maly = bez_mezery.lower()
# #palindrom = "martin"
# delka_palidromu_maly = len(bez_mezery_maly)
# print(bez_mezery_maly)
# print(delka_palidromu_maly)


# def palindrom_pozpatku(bez_mezery_maly):
#     palindrom_pozpatku = ""
#     for i in range (len(bez_mezery_maly)):
#         char = bez_mezery_maly[0 - i - 1]
#         palindrom_pozpatku = palindrom_pozpatku + char
#         #print(palindrom_pozpatku)

#     return(palindrom_pozpatku)

# print(palindrom_pozpatku(bez_mezery_maly))



# if bez_mezery_maly == palindrom_pozpatku(bez_mezery_maly):
#     print(True)
# else: 
#     print(False)

###################################################################################

# Cvičení 3.4: Zvýrazňovač
# Úkol:
# Na vstupu bude zadáno jedno slovo, mezera, a pak celá věta. Vypište tuto větu na
# výstup, s tím, že každý výskyt zadaného slova bude vypsán velkými písmeny.
# Vzorový vstup 1:   Vzorový vstup 2:  
# oko Mám oko špinavé od čokolády. jelen Pivo jelenům nenaléváme!
# Vzorový výstup 1:   Vzorový výstup 2:  
# Mám OKO špinavé od čOKOlády. Pivo JELENům nenaléváme!
""" 
slovo = "oko"
veta = "Mam oko spinave od cokolady"

slovo = "oko"
slovnik = {}

# for pismeno in slovo:
#     velke_pismeno = pismeno.upper()
#     slovnik[pismeno] = velke_pismeno      
# print(slovnik)
# veta = "Toto je testovací věta"
# slovo = "oko"
# slovnik = {}

# Vytvoření slovníku, kde klíče jsou písmena ze slova a hodnoty jsou odpovídající velká písmena
for pismeno in slovo:
    velke_pismeno = pismeno.upper()
    slovnik[pismeno] = velke_pismeno

# Nahrazení písmen ve větě pomocí slovníku
nova_veta = ""
for znak in veta:
    if znak in slovnik:
        nova_veta += slovnik[znak]
    else:
        nova_veta += znak

print(nova_veta) """

##############################################################################################

# Otázky:
# text = 'Lorem ipsum dolor sit amet'
# Který z těchto výrazů vrátí True? 
# (A) text[5] == 'm'...........................False 
# (B) text[1:4] == 'orem'......................ore
# (C) ' ' in text..............................True
# (D) text.isalpha()
# Který z těchto výrazů vrátí True?
# (A) text.replace('n', 'f') == text...........false
# (B) text.strip('Lol') == text................false
# (C) 'abc' + 'def' == 'abc def'...............false
# (D) "5" * 5 == '55555'.......................true
# Který z těchto výrazů vrátí True?
# (A) 'Brrrrr no to je zima'.strip('Br').startswith('no')
# (B) 'Brno'.replace('r','rrrrr')[-1] == 'n'
# (C) 'Toto léto stojí za to'.count('to') <= 4
# (D) 'Brno'.find('r') == 'Olomouc'.find('o')

##############################################################################################
# Povinné domácí úkoly
# DÚ 3.1: Vědecký formát
# Úkol:
# Napište kód, který se standardního vstupu načte číslo a vypíše ho na výstup ve
# vědeckém formátu se dvěma desetinnými místy.
# Vzorový vstup:
# 40800000000.00000000000000
# Vzorový výstup:
# 4.08E+10

#vstupni_cislo = float(input("Zadej jakekoliv cislo: \n"))

# cislo = 40800000000.00000000000000
# #cislo = float(input())
# # Formátování čísla ve vědeckém formátu s dvěma desetinnými místy
# formatovane_cislo = "{:.2E}".format(cislo)
# print(formatovane_cislo)  

#########################################################################################

# DÚ 3.2: Hledáme mezeru
# Úkol:
# Ze standarního vstupu načtěte řetězec. Vypište první pozici mezery v tomto řetězci a
# tři znaky, které za ní následují. (Můžete předpokládat, že zadaný řetězec bude vždy
# obsahovat aspoň jednu mezeru.)
# Vzorový vstup:
# Zítra bude krásné počasí.

# retezec = "Zítra bude krásné počasí."
# # Najděte první pozici mezery
# prvni_mezera = retezec.find(" ")

# if prvni_mezera != -1 and prvni_mezera < len(retezec) - 3:
#     cast_retezce_po_mezere = retezec[prvni_mezera + 1 : prvni_mezera + 4]
#     print(f"Pozice první mezery: {prvni_mezera}")
#     print(f"Tři znaky po mezeře: {cast_retezce_po_mezere}")
# else:
#     print("Mezera nebyla nalezena nebo za ní není dostatek znaků.")

##########################################################################################

# DÚ 3.3: Generátor výmluv
# Úkol:
# Ze standarního vstupu načtěte dva řádky. Z nich vygenerujte výmluvu a vypište (viz
# vzorový výstup).
# Vzorový vstup 1:   Vzorový vstup 2:  
# umýt nádobí dělat úkol z Pythonu
# musím chytat Pokémony venku je moc hezky
# Vzorový výstup 1:   Vzorový výstup 2:  
# Bohužel nemůžu umýt nádobí,
# protože musím chytat Pokémony.
# Bohužel nemůžu dělat úkol z
# Pythonu, protože venku je moc
# hezky.

# povinnost = "umyt nadobi"
# vymluva = "musim chytat pokemony"
# # Nemuzu umyt nadobi, prototoze musim chytat pokemony.
# vysledek = print(f"Nemuzu {povinnost}, protoze {vymluva}.")
# povinnost_1 = input("Napis co musim:\n")
# vymluva_1 = input("Napis na co se vymlouvam: \n")
# vysledek_1 = print(f"Bohuyel nemuzu {povinnost_1}, protoze {vymluva_1}.")

#################################################################################################

# DÚ 3.4: DNA
# Sekvence DNA se skládá ze čtyř typů nukleových bazí (A, C, G, T). Absolutní četnost
# báze vyjádřuje, kolikrát se vyskytuje daná báze v sekvenci.
# Úkol:
# Ze standardního vstupu načtěte sekvenci DNA. Na výstup vypište absolutní četnosti
# jednotlivých bazí.


# dna = input("Zadej sekvenci DNA: \n")   #"ACGTTTTGAG"

# a = dna.count('A')
# print(f"'A' : {a}")
# c = dna.count('C')
# print(f"'C' : {c}")
# g = dna.count('G')
# print(f"'G' : {g}")
# t = dna.count('T')
# print(f"'T' : {t}")

########################################################################################

# DÚ 3.5: DNA podruhé
# Relativní četnost báze vyjádřuje, jaká část sekvence (kolik procent) je tvořena daným
# typem báze.
# Úkol:
# Ze standardního vstupu načtěte sekvenci DNA. Na výstup vypište relativní četnosti
# jednotlivých bazí v procentech. Zaokrouhlujte na celá procenta.
# Poznámka: Formát .0% zde nebude fungovat, protože vypisuje procenta bez mezery.
# Musíte si poradit jinak.
# Vzorový vstup 1:   Vzorový vstup 2:  
# ACGTTTTGAG AAAACCCCTTTTTTTTTT
# Vzorový výstup 1:   Vzorový výstup 2:  
# A: 20 % A: 22 %
# C: 10 % C: 22 %
# G: 30 % G: 0 %
# T: 40 % T: 56 

#dna = input("Zadej sekvenci DNA: \n")   #"ACGTTTTGAG"
#dna = "ACGTTTTGAG"
dna = "AAAACCCCTTTTTTTTTT"
a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')

celkem  = a + c + g + t
print(f"'A' : {round(a/celkem*100)} %")
print(f"'C' : {round(c/celkem*100)} %")
print(f"'G' : {round(g/celkem*100)} %")
print(f"'T' : {round(t/celkem*100)} %")







