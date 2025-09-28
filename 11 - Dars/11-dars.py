# 11 - Dars | Shart Operatorlari (if, elif, else)

# Oddiy if operatori
yosh = 20

if yosh == 20:
    print("Siz voyaga yetgansiz!")


##
yosh = 17

if yosh >= 18:
    print("Siz voyaga yetgansiz!")
else:
    print("Siz hali voyaga yetmagansiz!")


###
baho = 10

if baho >= 90:
    print("A'lo!")
elif baho >= 80:
    print("Yaxshi!")
elif baho >= 70:
    print("Qoniqarli!")
elif baho == 10:
    print("ajoyib")
else:
    print("Qoniqarsiz!")


####
yosh = 2
jins = "ayol"

if yosh >= 18:
    if jins == "erkak":
        print("Siz erkak va voyaga yetgansiz!")
    else:
        print("Siz ayol va voyaga yetgansiz!")
else:
    print("Siz hali voyaga yetmagansiz!")


#####
yosh = 17
kitob_soni = 5

if yosh >= 18 and kitob_soni >= 3:
    print("Siz kutubxona a'zoligiga ega bo'lish huquqiga egasiz!")
else:
    print("Siz kutubxona a'zoligiga ega bo'lish huquqiga ega emassiz!")

yoki
if yosh < 18 or kitob_soni < 3:
    print("Siz kutubxona a'zoligiga ega bo'lish huquqiga ega emassiz!")
else:
    print("Siz kutubxona a'zoligiga ega bo'lish huquqiga egasiz!")



#AMALI 1

baho = int(input("Bahongizni kiriting (0-100): ")) #baho = 95

if baho >= 90:
    daraja = "A'lo"
    izoh = "A'lo natija! 🎉"
elif baho >= 80:
    daraja = "Yaxshi"
    izoh = "Yaxshi natija! 👍"
elif baho >= 70:
    daraja = "Qoniqarli" 
    izoh = "Qoniqarli natija! ✅"
elif baho >= 60:
    daraja = "Qoniqarsiz"
    izoh = "Yaxshiroq harakat qilishingiz kerak! 📚"
else:
    daraja = "Yomon"
    izoh = "Qayta o'qishingiz kerak! ⚠️"

print(f"Bahongiz: {baho}")
print(f"Daraja: {daraja}")
print(f"Izoh: {izoh}")


#AMALI 2
print("Bankimizga xush kelibsiz! 🏦")

balans = 1000000
parol = "1234"

foydalanuvchi_parol = input("Parolingizni kiriting: ")

if foydalanuvchi_parol == parol:
    print("Xush kelibsiz!")
    
    amal = input("Amal tanlang (1: Balans, 2: Pul yechish, 3: Pul qo'shish): ")
    
    if amal == "1":
        print(f"Sizning balansingiz: {balans} so'm")
        
    elif amal == "2":
        miqdor = int(input("Yechmoqchi bo'lgan miqdoringiz: "))
        if miqdor <= balans:
            balans -= miqdor
            print(f"{miqdor} so'm yechildi. Yangi balans: {balans} so'm")
        else:
            print("Balansingizda yetarli mablag' yo'q!")
            
    elif amal == "3":
        miqdor = int(input("Qo'shmoqchi bo'lgan miqdoringiz: "))
        balans += miqdor
        print(f"{miqdor} so'm qo'shildi. Yangi balans: {balans} so'm")
        
    else:
        print("Noto'g'ri amal tanlandi!")
        
else:
    print("Noto'g'ri parol! Iltimos, qayta urinib ko'ring.")
