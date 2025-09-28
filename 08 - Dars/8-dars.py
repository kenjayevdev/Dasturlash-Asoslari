# 08 - Dars | Ro'yxatlar (Lists) Pythonda Ma'lumotlar Strukturasi


# Oddiy ro'yxatlar
mevalar = ["olma", "banan", "nok", "anor"]
sonlar = [1, 2, 3, 4, 5]
aralash = ["matn", 42, 3.14, True]

print(mevalar)
print(sonlar)   
print(aralash)


#2
mevalar = ["olma", "banan", "nok", "anor", "uzum"]

#Indeks orqali murojaat
print(mevalar[0])   
print(mevalar[1])
print(mevalar[2])
print(mevalar[4])

#Salbiy indekslar (oxiridan boshlab)
print(mevalar[-1])
print(mevalar[-2])
print(mevalar[-4])

#3
mevalar = ["olma", "banan", "nok", "anor", "uzum", "shaftoli"]

print(mevalar[1:4]) 
print(mevalar[:3])
print(mevalar[2:])
print(mevalar[::2])
print(mevalar[::-1])



#4
mevalar = ["olma", "banan", "nok"]

# append() - oxiriga element qo'shadi
mevalar.append("anor")
print(mevalar)

# insert() - belgilangan joyga element qo'shadi
mevalar.insert(1, "uzum")
print(mevalar)

# extend() - boshqa ro'yxatni qo'shadi
yangi_mevalar = ["shaftoli", "gilos","anjir"]
mevalar.extend(yangi_mevalar)
print(mevalar)



#5
mevalar = ["olma", "banan", "nok", "anor", "uzum"]

# remove() - belgilangan qiymatli elementni o'chiradi
mevalar.remove("banan")
print(mevalar)

# pop() - belgilangan indeksdagi elementni o'chiradi
mevalar.pop()
print(mevalar)

# pop() - indeks berilmasa oxirgi elementni o'chiradi
mevalar.pop()
print(mevalar)

# del - indeks orqali elementni o'chiradi
del mevalar[3]
print(mevalar)

# clear() - ro'yxatni tozalaydi
mevalar.clear()
print(mevalar)



#6
raqamlar = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - ro'yxatni saralaydi
raqamlar.sort()
print(raqamlar)

# reverse() - ro'yxatni teskari aylantiradi
raqamlar.reverse()
print(raqamlar)

index() - element indeksini qaytaradi
print(raqamlar.index(5))

# count() - element necha marta takrorlanganini qaytaradi
print(raqamlar.count(1))

# copy() - ro'yxatning nusxasini yaratadi
nusxa = raqamlar.copy()
print(nusxa)

# len() - ro'yxat uzunligini qaytaradi
print(len(raqamlar))



#7
mevalar = ["olma", "banan", "nok", "anor"]

# in operatori - element mavjudligini tekshiradi
print("olma" in mevalar)
print("uzum" in mevalar)

# not in operatori - element mavjud emasligini tekshiradi
print("uzum" not in mevalar)
print("olma" not in mevalar)


#8
# Ro'yxatlarni qo'shish
list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlashma = list1 + list2
print(birlashma)

# Ro'yxatlarni ko'paytirish
takror = list1 * 3
print(takror)




# Amaliy
# Mahsulotlar ro'yxati
mahsulotlar = ["non", "sut", "guruch", "go'sht", "choy"]

print("Do'konimizdagi mahsulotlar:")
for i, mahsulot in enumerate(mahsulotlar):
    print(f"{i+1}. {mahsulot}")

#Yangi mahsulot qo'shish
yangi_mahsulot = input("Yangi mahsulot nomini kiriting: ")
mahsulotlar.append(yangi_mahsulot)

print(f"\nYangi ro'yxat:")
for i, mahsulot in enumerate(mahsulotlar):
    print(f"{i+1}. {mahsulot}")

#Mahsulotni qidirish
qidiruv = input("Qidirmoqchi bo'lgan mahsulotingiz: ")
if qidiruv in mahsulotlar:
    print(f"{qidiruv} do'konimizda mavjud!")
else:
    print(f"Kechirasiz, {qidiruv} hozir mavjud emas.")