# 13 - Dars | For Tsikli (Ro'yxatlar Ustida Aylanish)


# Oddiy for tsikli
mevalar = ["olma", "banan", "nok", "anor", "shaftoli"]

for meva in mevalar:
    print(f"Men {meva}ni yaxshi ko'raman!")
    
    
#
# Range() funksiyasi misollari
print("0 dan 4 gacha:")
for i in range(1,11):
    print(i)

print("\n2 dan 7 gacha:")
for i in range(2, 8):
    print(i)

print("\n1 dan 9 gacha, 2 qadam bilan:")
for i in range(1, 20, 2):
    print(i)



##
talaba = {
    "ism": "Ali",
    "yosh": 20,
    "kurs": 3,
    "fakultet": "Dasturlash"
}

print("Faqat kalitlar:")
for kalit in talaba:
    print(kalit)

print("\nFaqat qiymatlar:")
for qiymat in talaba.values():
    print(qiymat)

print("\nKalit va qiymatlar:")
for kalit, qiymat in talaba.items():
    print(f"{kalit}: {qiymat}")
    
    

###
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Break misoli (6 ga yetganda to'xtaydi):")
for son in sonlar:
    if son == 9:
        print("8 ga yetdik, tsikl to'xtaydi!")
        break
    print(son)

print("\nContinue misoli (juft sonlarni o'tkazib yuboradi):")
for son in sonlar:
    if son % 2 == 0:
        continue
    print(son)
    
    
    
#### AMALIY

talabalar = ["Ali", "Vali", "Hasan", "Husan", "Azizbek"]
baholar = {}

print("Talabalar baholari kiritish:")
for talaba in talabalar:
    baho = int(input(f"{talaba}ning bahosi (0-100): "))
    baholar[talaba] = baho

print("\nTalabalar baholari:")
for talaba, baho in baholar.items():
    print(f"{talaba}: {baho}")

# O'rtacha baho
ortalama = sum(baholar.values()) / len(baholar)
print(f"\nO'rtacha baho: {ortalama}")

