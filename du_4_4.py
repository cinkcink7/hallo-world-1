
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
# Mama mele maso Venku je vetrno





