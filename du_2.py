
import math
print("hallo world")

#Syntax a matematicke operatory

#parita

""" a = 2 ** 8
b = 5 + 5
c = 10 * 5 * 5
d = 5
celkovy_vysledek =  2**8 - (5 + 5) * 5 * 5 + 5 # 
# pozn 256 - (250) + 5 
print(a)
print(b)
print(c)
print(d)

print(celkovy_vysledek) """

#ukoly 

""" Otázky:
Které z těchto čísel je největší?
• A) 5/3
• B) 5//3
• C) 5%3
• D) 5,3 
D ... 5,3  je nejvestsi
"""


list_alfa = [5/3, 5//3, 5%3, 5.3]
nejvetsi_cislo = list_alfa[0]  # Předpokládáme, že první prvek je nejvetsi

for cislo in list_alfa:
    if cislo > nejvetsi_cislo:
        nejvetsi_cislo = cislo

print("Nejmenší číslo v listu je:", nejvetsi_cislo)


""" Které z těchto čísel je nejmenší?
• A) 6.12
• B) 6.1e2
• C) 6.1 e 2 # tohle budu syntax error
• D) 6.1 ** 2 """

list_alfa = [6.12, 6.1e2, 6.1 ** 2]
nejmensi_cislo = list_alfa[0]  # Předpokládáme, že první prvek je nejmenší

for cislo in list_alfa:
    if cislo < nejmensi_cislo:
        nejmensi_cislo = cislo

print("Nejmenší číslo v listu je:", nejmensi_cislo)


##########################################################################################


""" Otázky:
a, b = 5, 2
a += b
b = a
a -= 1
Co bude v proměnných a, b po vykonání uvedeného kódu?
• A) 5, 2
• B) 1, 2
• C) 6, 7
• D) 6, 6 """

a, b = 5, 2

print(a)
print("**************************************************")
print(b)
print("**************************************************")
a += b
print(a)
print("**************************************************")
b = a
print(b)
print("**************************************************")
a -= 1
# print(a)
# print("**************************************************")
sin_nula = math.sin(0)
sin_tricet = math.sin(30)
sin_ctyricetpet = math.sin(45)
sin_sedesat = math.sin(60)
sin_devadesat = math.sin(90)

print(sin_nula ,sin_tricet , sin_ctyricetpet, sin_sedesat , sin_devadesat)

####################################################################################################

# Otázky:
# Který z těchto příkazů vypíše na výstup 200?
# • A) print 200
# • B) print(100+100)
# • C) print('100+100')
# • D) print(float(200))

print(float(200))
print(100+100)

# Která z těchto hodnot je typu int?
# • A) int***********************to neni nic
# • B) type(int)*****************to vypise co je tam za typ...jestli to beru jako ze int je integer cele nejake cislo pak 
# • C) int(24/7)***************** y toho vzpadne float
# • D) '9'***********************tohle je vlastne string
# Logické hodnot

#####################################################################################################
print("*****************   procviceni   *****************************")
### PROCVICENI ###

print(2**2 == 2*2)
print(5e-6 >= abs(-5e6))
import math
print(type(10/2) == type(math.pi))
print(10/2)
print(type(math.pi))
######################################################################################################
print("  * ********************************************************* * ")
x = 5 #5
print(x)
x -= 1#4
print(x)
x *= x#16
print(x)
y = 10 - x#--6
print(y)
y > 0#false
print(y>0)
print("  * ********************************************************* * ")
######################################################################################################

n = 20#20
n_lost = 7#7
n_final = n - n_lost#13
n_final != 13#false

print(n_final !=13)

print("  * ********************************************************* * ")
######################################################################################################

height = width = 10#10
area = height * width#100
#a = height > 5 and area = 100#True***************tady to nebere syntaxi

if height > 5 and area == 100:
    print("mas to spravne")

print("  * ********************************************************* * ")
######################################################################################################

a = True
b = False
a and b or not a and not b # true a zaroven false nebo false a zaroven true-------------co tim chce rict?dej priklad

print(a and b or not a and not b)
print("  * ********************************************************* * ")
######################################################################################################

x = 5
y = 10
y < x * x or y <= 2 * x and x > y# true krat pet nebo 10 vetsi nebo rovno deset a zaroven true
# true nebo true a zaroven true ********* jak to ze kdyz udelam false true false ... je to co? ja myslim false
print("sakra co")
print(y < x * x or y >= 2 * x and x > y)

print("  * ********************************************************* * ")
######################################################################################################


# Nepovinné úkoly
# Cvičení 2.1: Obdélník
# V této ukázce si napíšeme program pro výpočet obvodu a povrchu obdélníku:
# Obvod 𝑜 a povrch 𝑆 obdélníku o stranách 𝑎, 𝑏 můžeme spočítat podle vzorců:
# 𝑜 = 2𝑎 + 2𝑏
# 𝑆 = 𝑎𝑏
# Úkol:
# Spočítejte obvod a povrch obdélníku o stranách a, b. Výsledky uložte do proměnných
# o, S.
# (O vstup a výstup se stará předpřipravený kód. Tj. první řádek kódu vám zobrazí
# okénko, do kterého vpíšete vzorový vstup (nebo jiný vstup), a zadané hodnoty se uloží
# do proměnný

""" a = float(input("Napis zde prvni stranu obdelnika"))
b = float(input("Napis zde druhou stranu obdelnika"))

def obvod(a, b):
    obvod = 2*a + 2*b
    return obvod

def obsah(a, b):
    obsah = a * b
    return obsah


vypocitany_obvod = obvod(a, b)
vypocitany_obsah = obsah(a, b)

print(f"Zde jsou tve vypocty, obsah obdelnika je {vypocitany_obsah} a jeho obvod je {vypocitany_obvod}") """

print("  * ********************************************************* * ")
######################################################################################################

# Cvičení 2.2: Pravoúhlý trojúhelník
# Mějme pravoúhlý trojúhelník 𝐴𝐵𝐶 s odvěsnami 𝑎, 𝑏 a přeponou 𝑐. Pro úhel 𝛼 platí tyto
# vztahy:
# sin 𝛼 =
# 𝑎
# 𝑐
# cos 𝛼 =
# 𝑏
# 𝑐
# tan 𝛼 =
# 𝑎
# 𝑏
# Úkol:
# Ze zadaných délek odvěsen a, b spočítejte velikost úhlu 𝛼 ve stupních. Výsledek uložte
# do proměnné alpha. (O vstup a výstup se stará předpřipravený kód.)
# Vzorový vstup:
# 10 20
# Vzorový výstup:
# 26.565




print("  * ********************************************************* * ")
######################################################################################################
""" a = float(input("Zadej odvesnu a: \n"))
b = float(input("Zadej odvesnu b: \n"))
c = float(input("Zadej preponu c: \n"))


sin_alfa = a/c
cos_alfa = b/c
tg_alfa = a/b

print(math.sin(sin_alfa))
print(math.cos(cos_alfa))
print(math.tan(tg_alfa))
print("*********************************************")
print(math.degrees(sin_alfa))
print(math.degrees(cos_alfa))
print(math.degrees(tg_alfa))
 """

print("  * ********************************************************* * ")
######################################################################################################

# Cvičení 2.3: Oblíbené číslo
# Alice, Bob a Cyril si chtějí vybrat společné oblíbené číslo.
# • Alici se líbí dvouciferná čísla, která obsahují čtyřku.
# • Bobovi se líbí čísla dělitelná třemi.
# • Cyrilovi se líbi všechna čísla kromě násobků sedmi
 
from random import randint
####

""" cislo = randint(1, 21)
print(cislo) 

def alice_fnc_ctyrka():

    #tohle je podminka na 4 v cisle
    alice_ctyrka = str(cislo)
    if "4" in alice_ctyrka:
        return True
    return False
   

def alice_fnc():
    alice = cislo
    if alice >= 10 and alice <=30:  
        return True
    return False
    
def bob_fnc():
    bob = cislo
    if bob % 3 == 0:
        return True
    return False
    
def cyril_fnc():
    cyril  = cislo
    if cyril % 7 != 0:
        return True
    return False

def vsichni_spokojeni(cislo):   
    if (alice_fnc() and bob_fnc() and cyril_fnc() and alice_fnc_ctyrka()):

        return True
    return False

while True:
    cislo = randint(1, 30)
    print(cislo)
    
    if vsichni_spokojeni(cislo):
        print(f"Nalezeno požadované číslo: {cislo}")
        break """

print("  * ********************************************************* * ")
######################################################################################################


#     Povinné domácí úkoly
# DÚ 2.1: Obvod trojúhelníku
# Úkol:
# Vypočítejte obvod trojúhelníku se stranami o délkách a, b, c. Výsledek uložte do
# proměnné o.
# Vzorový vstup:
# 2 3 4

""" a = int(input("Napis mi zde stranu a : \n "))
b = int(input("Napis mi zde stranu b: \n "))
c = int(input("Napis i zde stranu c: \n"))
5
def obvod_trojuhlenika(a, b, c):
    o = a + b + c
    return o

print(f" Obvod trojuhlenika je : {obvod_trojuhlenika(a, b, c)}") """
print("  * ********************************************************* * ")
######################################################################################################

# DÚ 2.2: Objem kužele
# Úkol:
# Vypočítejte objem kužele s poloměrem podstavy r a výškou v. Výsledek uložte to
# proměnné V.
# 𝑉 = 1
# 3
# ⋅ 𝜋 ⋅ 𝑟2
# ⋅ 𝑣
# Vzorový vstup:
# 3.5 12.0

""" from math import pi

polomer_podstavy = float(input("Zadej polomer podstavy: \n"))
vyska_kuzele = float(input("Zadej vysku kuzele: \n"))

V = 1/3 * (pi * polomer_podstavy ** 2 * vyska_kuzele)

print(round(V, 2)) """

print("  * ********************************************************* * ")
######################################################################################################

# DÚ 2.3: Pythagorova věta
# Úkol:
# Vypočítejte délku přepony c pravoúhlého trojúhelníku z délek odvěsen a, b podle
# Pythagorovy věty:
# 𝑎
# 2 + 𝑏2 = 𝑐2

""" from math import sqrt
a = float(input("Napis delku odvesny a: \n"))
b = float(input("Napis delku odvesny b: \n"))
c = sqrt(a ** 2 + b **2)
print(round(c, 2)) """

print("  * ********************************************************* * ")
######################################################################################################

# DÚ 2.4: Přepočet času
# Úkol:
# Čas t (v sekundách) vyjádřete jako počet celých hodin, minut a sekund. Výsledek
# uložte do proměnných hours, minutes, seconds. (O hezký výpis se postará před připravený poslední řádek.)
# Nápověda: využijte operátory // a %.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 90 3600
# Vzorový výstup 1:   Vzorový výstup 2:  
# 0:01:30 1:00:00



t = int(input("Zde mi napis sekund, a ja ti reknu kolik je to hodin a minut a sekund to je: \n"))

hours = t // 3600
zbytek_h = t - (hours *3600)
minutes = zbytek_h // 60
seconds = zbytek_h -(60 * minutes)



print(hours)
print(minutes)
print(seconds)

print(f'{hours}:{minutes:02}:{seconds:02}')
      
print("  * ********************************************************* * ")
######################################################################################################

""" Dále vás prosím, aby jste nahrávali své domácí úkoly pod názvem du_x.ipynb, kde
x je číslo přednášky na které byl domácí úkol zadán. Zkrátka tak, jak je psáno v
interaktivní osnově. V opačném případě nejsem schopen zaručit, že body za domácí
úkoly dostanete, protože moje skripty na opravování domácích úkolu mohou mít
potíže.
 """
