# 15 - Dars | Modullar (Python kutubxonalari bilan ishlash)



# O'z modulimizdan foydalanish
from foydali_modul import salom_ber, kvadrat_top

print(salom_ber("Ali"))
print(f"20 ning kvadrati: {kvadrat_top(20)}")


# Math modulini import qilish
import math

# Math modulidagi funksiyalardan foydalanish
print(f"Pi soni: {math.pi}")
print(f"10 ning ildizi: {math.sqrt(10)}")
print(f"6 ning 2-darajasi: {math.pow(6, 2)}")


##
# 1. To'liq import
import math
print(math.sqrt(16))

# 2. Boshqa nom bilan import
import math as m
print(m.sqrt(16))

# 3. Faqat kerakli funksiyalarni import
from math import sqrt, pi
print(sqrt(16))
print(pi)

# 4. Barchasini import qilish (ehtiyot bo'ling!)
from math import *
print(sqrt(16))


# Dir() funksiyasi
import math

# Math modulidagi barcha funksiyalarni ko'rish
print("Math moduli funksiyalari:")
for funksiya in dir(math):
    if not funksiya.startswith('_'):  # Maxsus funksiyalarni o'tkazib yuborish
        print(funksiya)

# Faqat o'zimizga kerak bo'lgan funksiyalarni tekshirish
print(f"\nsqrt funksiyasi mavjud: {'sqrt' in dir(math)}")
print(f"pi o'zgaruvchisi mavjud: {'piss' in dir(math)}")


####
import random

# Tasodifiy sonlar
print(f"1-10 orasida tasodifiy son: {random.randint(1, 10)}")
print(f"0-1 orasida tasodifiy son: {random.random():.2f}")

# Tasodifiy tanlov
mevalar = ["olma", "banan", "nok", "anor"]
print(f"Tasodifiy meva: {random.choice(mevalar)}")
print(f"Tasodifiy 2 ta meva: {random.sample(mevalar, 2)}")

# Aralash tartib
random.shuffle(mevalar)
print(f"Aralangan mevalar: {mevalar}")



#####
from datetime import datetime, timedelta

# Hozirgi vaqt
hozir = datetime.now()
print(f"Hozirgi vaqt: {hozir}")
print(f"Yil: {hozir.year}, Oy: {hozir.month}, Kun: {hozir.day}")

# Vaqt formati
print(f"Formatlangan vaqt: {hozir.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Soat: {hozir.hour}:{hozir.minute}")

# Vaqt orqaga va oldinga
bir_kun_oldinga = hozir - timedelta(days=1)
bir_hafta_keyin = hozir + timedelta(weeks=1)
print(f"Bir kun oldin: {bir_kun_oldinga}")
print(f"Bir hafta keyin: {bir_hafta_keyin}")


###### AMALIY
import random

def tasodifiy_tavsiya():
    # Turli sohalardagi tavsiyalar
    kitoblar = ["Atom Odatlar", "Muqaddima", "Jinoyat va Jazo", "Hokimiyatning 48 qoidasi"]
    kinolar = ["qashqirlar makoni", "men kimman", "Xavfli Biznes", "Temur"]
    taomlar = ["Osh", "Mastava", "Lag'mon", "Somsa", "Shashlik"]
    mashgulotlar = ["Yugurish", "Suzish", "kurash", "Futbol", "Basketbol"]
    
    print("Tasodifiy Tavsiyalar Generatori 🎲")
    print("1. Kitob tavsiyasi")
    print("2. Kino tavsiyasi") 
    print("3. Taom tavsiyasi")
    print("4. Mashg'ulot tavsiyasi")
    print("5. Hammasi birdan")
    
    tanlov = input("Tanlovingiz (1-5): ")
    
    if tanlov == "1":
        print(f"Kitob tavsiyasi: {random.choice(kitoblar)}")
    elif tanlov == "2":
        print(f"Kino tavsiyasi: {random.choice(kinolar)}")
    elif tanlov == "3":
        print(f"Taom tavsiyasi: {random.choice(taomlar)}")
    elif tanlov == "4":
        print(f"Mashg'ulot tavsiyasi: {random.choice(mashgulotlar)}")
    elif tanlov == "5":
        print(f"Kitob: {random.choice(kitoblar)}")
        print(f"Kino: {random.choice(kinolar)}")
        print(f"Taom: {random.choice(taomlar)}")
        print(f"Mashg'ulot: {random.choice(mashgulotlar)}")
    else:
        print("Noto'g'ri tanlov!")

# Dasturni ishga tushirish
tasodifiy_tavsiya()