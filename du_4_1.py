
# du_X_Y.py

# Ú 4.1: Začíná, končí nebo obsahuje?
# Úkol:
# Na vstupu získáte dva řetezce oddělené mezerou. Otestujte jestli první řetězec začíná,
# končí nebo aspoň obsahuje druhý řetězec. Možné výstupy:
# • '…' starts and ends with '…'
# • '…' starts with '…'
# • '…' ends with '…'
# • '…' contains '…'
# • '…' does not contain '…'
# (Místo … doplňte první a druhý řetězec.)
# Vzorový vstup:
# alobal al
# Vzorový výstup:
# 'alobal' starts and ends with 'al'
# Vyzkoušejte také tyto vstupy:
# bussiness bus
# autobus bus
# alobal oba
# alobal bus

retezec = input("Zadej dve reteyzce oddělená mezerami: ").split()

if len(retezec) != 2:
    print("Zadal jsi jeden retezec.")

elif len(retezec) >= 2:
    r = str(retezec[0])
    #print(r)
    v = str(retezec[1])
    #print(v)

    zacatek_r = r[0]
    #print(zacatek_r)
    konec_r = r[len(r)-1]
    #print(konec_r)

    zacatek_v = v[0]
    #print(zacatek_v)
    konec_v = r[len(v)-1]
    #print(konec_v)

    if zacatek_r == zacatek_v and konec_r == konec_v:
        print(f" {r} + start with {zacatek_r} end with {konec_r}")

