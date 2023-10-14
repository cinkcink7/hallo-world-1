
# du_X_Y.py
# DÚ 4.4: Caesarova šifra
# Caesarova šifra spočívá v posunu každého písmena o pevný počet pozic v abecedě.
# Tento počet se nazývá klíč.
# Například je-li klíč 2, pak posouváme o 2 pozice doprava a písmeno B se změní na D.
# Zpráva Hello World se zašifruje na Jgnnq Yqtnf. Když chceme zprávu rozšifrovat,
# musíme ji posunout o stejný počet pozic zpátky doleva.
# Záporný klíč znamená posun opačným směrem, tj. zašifrování doleva, rozšifrování
# doprava.

# Na vstupu získate klíč a zašifrovanou zprávu (mezi nimi znak #). Zprávu rozšifrujte a
# vypište.
# Mezery mezi písmeny nechte beze změny. Ke kódování používáme standardní anglickou abecedu, která má pořadí 
# stejné jako znakové sady ASCII nebo Unicode.
# Nemusíte řešit přetečení (tj. že například znak Z by se posunul zpátky na začátek
# abecedy na B).
# Nápověda: Použijte funkce chr a ord (viz konec přednášky Řetězce). Při výpisu
# můžete využít funkci print s parametrem end='' (nezalamuje výstup na nové řádky).
# Vzorový vstup 1:   Vzorový vstup 2:  
# 5#Rfrf rjqj rfxt -3#Sbkhr gb sbqokl
# Vzorový výstup 1:   Vzorový výstup 2:  
# Mama mele maso      Venku je vetrno

""" 
def caesar_sifra(text, klic):
    zasifrovany_text = ""
    klic = int(klic)  # Převod klíče na celé číslo

    for pismeno in text:
        if pismeno.isalpha():
            if pismeno.islower():
                zasifrovany_pismeno = chr(((ord(pismeno) - ord('a') + klic) % 26) + ord('a'))
            else:
                zasifrovany_pismeno = chr(((ord(pismeno) - ord('A') + klic) % 26) + ord('A'))
        else:
            zasifrovany_pismeno = pismeno

        zasifrovany_text += zasifrovany_pismeno

    return zasifrovany_text

retezec = input("Zadej klic a text oddeleny '#' znakem: ")
klic, text = retezec.split('#')

zasifrovany_text = caesar_sifra(text, klic)
print("Zašifrovaný text:", zasifrovany_text)

rozsifrovany_text = caesar_sifra(zasifrovany_text, -int(klic))
print("Rozšifrovaný text:", rozsifrovany_text)
 """
# Jgnnq Yqtnf

def rozsifruj_zpravu(klic, zprava):
    rozsifrovana_zprava = ""

    for pismeno in zprava:
        if pismeno.isalpha():
            if pismeno.islower():
                rozsifrovane_pismeno = chr(((ord(pismeno) - ord('a') - int(klic)) % 26) + ord('a'))
            else:
                rozsifrovane_pismeno = chr(((ord(pismeno) - ord('A') - int(klic)) % 26) + ord('A'))
        else:
            rozsifrovane_pismeno = pismeno

        rozsifrovana_zprava += rozsifrovane_pismeno

    return rozsifrovana_zprava

vstup = input("Zadej klíč a zašifrovanou zprávu oddělenou '#': ")
klic, zprava = vstup.split('#')

rozsofrovana_zprava = rozsifruj_zpravu(klic, zprava)
print(rozsofrovana_zprava)

#-3#Sbkhr gb sbqokl