# 12 - Dars | While Tsikli (Takrorlanuvchi Amallar)


# Oddiy while tsikli
sanoq = 1

while sanoq < 10:
    print(f"Sanoq: {sanoq}")
    sanoq += 1

print("tskil tugadi")


##
# Break misoli
sanoq = 1

while sanoq <= 10:
    
    if sanoq == 5:
        print("5 ga yetdik, tsikl to'xtaydi!")
        break
    print(f"Sanoq: {sanoq}")
    sanoq += 1

Continue misoli
sanoq = 0

while sanoq < 10:
    sanoq += 1
    if sanoq % 2 == 0:
        continue
    print(f"Toq son: {sanoq}")


###

# To'g'ri usul
sanoq = 1
while True:
    print(f"Sanoq: {sanoq}")
    sanoq += 1

    if sanoq > 5:
        break


#### AMALIY
print("Tizimga kirish 🔐")

to_gri_parol = "python123"
urinishlar = 3

while urinishlar > 0:
    parol = input("Parolni kiriting: ")
    
    if parol == to_gri_parol:
        print("Xush kelibsiz! Tizimga kirdingiz. ✅")
        break
    else:
        urinishlar -= 1
        print(f"Noto'g'ri parol! {urinishlar} urinish qoldi. ❌")
        
        if urinishlar == 0:
            print("Hisobingiz bloklandi! Xavfsizlik xizmatiga murojaat qiling. ⚠️")