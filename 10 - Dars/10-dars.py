# 10 - Dars | Tuple va Set (O'zgarmas ro'yxat va To'plamlar)


# Tuple yaratish
mevalar = ("olma", "banan", "nok", "shaftoli","tarvuz","yong'oq")
raqamlar = (1, 2, 3, 4, 5, 6, 7,8)

print(type(mevalar))
print(raqamlar)

mevalar[0] = "apelsin"
mevalar.append("uzum")



##
mevalar = ("olma", "banan", "nok", "shaftoli")

print(mevalar[0])
print(mevalar[1])
print(mevalar[-1])


###
# Set yaratish
mevalar_set = {"olma", "banan", "nok", "olma", "nok"}
raqamlar_set = {1, 2, 3, 2, 1, 6}

print(mevalar_set)
print(raqamlar_set)


####
mevalar_set = {"olma", "banan", "nok", "olma"}
mevalar_set.add("uzum")
print(mevalar_set)

mevalar_set.remove("banan")
print(mevalar_set)


#####
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

birlashma = set_a | set_b
print(birlashma)

kesishma = set_a & set_b
print(kesishma)

farq = set_a - set_b
print(farq)


#AMALIY

# Do'kon inventarizatsiyasi

# O'zgarmas mahsulotlar ro'yxati (tuple)
mahsulotlar = ("non", "sut", "guruch", "go'sht", "choy")

# Mavjud mahsulotlar (set)
ombor = {"non", "sut", "guruch", "choy"}

print("Do'konimizdagi barcha mahsulotlar:")
for i, mahsulot in enumerate(mahsulotlar, 1):
    print(f"{i}. {mahsulot}")

print("\nHozir mavjud mahsulotlar:")
for mahsulot in ombor:
    print(f"- {mahsulot}")

# Yangi mahsulot qo'shish
yangi_mahsulot = input("\nYangi mahsulot nomi: ")
if yangi_mahsulot not in mahsulotlar:
    print("Kechirasiz, bu mahsulot do'konimizda mavjud emas")
else:
    ombor.add(yangi_mahsulot)
    print(f"{yangi_mahsulot} omborga qo'shildi")
