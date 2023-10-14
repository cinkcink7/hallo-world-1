
# du_X_Y.py

# DÚ 2.4: Přepočet času
# Úkol:
# Čas t (v sekundách) vyjádřete jako počet celých hodin, minut a sekund. Výsledek
# uložte do proměnných hours, minutes, seconds. (O hezký výpis se postará předpřipravený poslední řádek.)
# Nápověda: využijte operátory // a %.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 90 3600
# Vzorový výstup 1:   Vzorový výstu

sekund = int(input("Zadej pocet sekund: "))
hours = sekund // 3600
print(hours)
zbytek_po_hours = sekund - hours * 3600


minutes = zbytek_po_hours // 60
print(minutes)
seconds = zbytek_po_hours - minutes * 60 
print(seconds)

print(f"{hours:01d}:{minutes:02d}:{seconds:02d}")