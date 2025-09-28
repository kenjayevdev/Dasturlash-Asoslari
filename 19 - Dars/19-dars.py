# 19 - Dars | OOP Davomi (Meros, Polimorfizm va Kapsullash)

Asosiy (ota) class
class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi
    
    def ovoz_chiqar(self):
        return "Hayvon ovoz chiqarmoqda"
    
    def uxlash(self):
        return f"{self.nomi} uxlamoqda"
    
    def yugurish(self):
        return f"{self.nomi} yugurmogda"

# Meros oluvchi (bola) classlar
class Mushuk(Hayvon):  # Mushuk Hayvon classidan meros oladi
    def __init__(self, nomi, yoshi, rangi):
        super().__init__(nomi, yoshi)  # Ota classning konstruktorini chaqiramiz
        self.rangi = rangi
    
    def ovoz_chiqar(self):  # Metodni qayta yozish (override)
        return "Miyov-miyov!"
    
    def sichqon_ushlash(self):  # Yangi metod qo'shamiz
        return f"{self.nomi} sichqon ushlaydi"

class It(Hayvon):
    def __init__(self, nomi, yoshi, zanjirli):
        super().__init__(nomi, yoshi)
        self.zanjirli = zanjirli
    
    def ovoz_chiqar(self):
        return "Vov-vov!"
    
    def qoriqish(self):
        return f"{self.nomi} qo'riqlaydi"


mushuk = Mushuk("Mosh", 2, "oq")
it = It("Rex", 3, True)

# print(mushuk.ovoz_chiqar())
# print(it.ovoz_chiqar())

# print(mushuk.uxlash())       # Mosh uxlamoqda (ota classdan meros)
# print(mushuk.sichqon_ushlash())  # Mosh sichqon ushlaydi (yangi metod)

print(it.yugurish())         # Rex yugurmogda (ota classdan meros)
print(it.qoriqish())        # Rex qo'riqlaydi (yangi metod)





# ##
class Transport:
    def harakatlanish(self):
        pass

class Avtomobil(Transport):
    def harakatlanish(self):
        return "Avtomobil yo'lda yuryapti"

class Samalyot(Transport):
    def harakatlanish(self):
        return "Samalyot havoda uchyapti"

class Kema(Transport):
    def harakatlanish(self):
        return "Kema suzda suzyapti"

# Polimorfizmni ko'rsatamiz
transportlar = [Avtomobil(), Samalyot(), Kema()]

for transport in transportlar:
    print(transport.harakatlanish())

Yana bir misol
class Shakl:
    def yuzani_hisobla(self):
        pass

class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon
    
    def yuzani_hisobla(self):
        return self.tomon ** 2

class Aylana(Shakl):
    def __init__(self, radius):
        self.radius = radius
    
    def yuzani_hisobla(self):
        return 3.14 * self.radius ** 2

class Uchburchak(Shakl):
    def __init__(self, asos, balandlik):
        self.asos = asos
        self.balandlik = balandlik
    
    def yuzani_hisobla(self):
        return 0.5 * self.asos * self.balandlik

# Har xil shakllarning yuzasini hisoblaymiz
shakllar = [Kvadrat(5), Aylana(3), Uchburchak(4, 6)]

for shakl in shakllar:
    print(f"Yuzasi: {shakl.yuzani_hisobla()}")
    
    

###
class BankHisob:
    def __init__(self, ism, balans):
        self.ism = ism
        self.__balans = balans  # Private atribut (ikki pastki chiziq)
    
    # Getter metod - balansni o'qish
    def balansni_korsat(self):
        return f"Balans: {self.__balans} so'm"
    
    # Setter metod - balansni o'zgartirish (cheklov bilan)
    def pul_qoshish(self, miqdor):
        if miqdor > 0:
            self.__balans += miqdor
            return f"{miqdor} so'm qo'shildi"
        else:
            return "Miqdor musbat bo'lishi kerak"
    
    def pul_yechish(self, miqdor):
        if 0 < miqdor <= self.__balans:
            self.__balans -= miqdor
            return f"{miqdor} so'm yechildi"
        else:
            return "Noto'g'ri miqdor"

# Test qilamiz
hisob = BankHisob("Ali", 1000)

print(hisob.balansni_korsat())  # Balans: 1000 so'm
print(hisob.pul_qoshish(500))   # 500 so'm qo'shildi
print(hisob.pul_yechish(200))   # 200 so'm yechildi
print(hisob.balansni_korsat())  # Balans: 1300 so'm

# To'g'ridan-to'g'ri kirish mumkin emas
print(hisob.__balans)  # Xato! AttributeError



#### AMALIY

import random

class Qahramon:
    def __init__(self, nomi, salomatlik, hujum):
        self.nomi = nomi
        self._salomatlik = salomatlik  # Protected atribut
        self.hujum = hujum
        self.joriy_salomatlik = salomatlik
    
    def hujum_qilish(self):
        return random.randint(self.hujum - 5, self.hujum + 5)
    
    def zarar_olish(self, zarar):
        self.joriy_salomatlik -= zarar
        if self.joriy_salomatlik < 0:
            self.joriy_salomatlik = 0
    
    def tirikmi(self):
        return self.joriy_salomatlik > 0
    
    def holatni_korsat(self):
        return f"{self.nomi}: {self.joriy_salomatlik}/{self._salomatlik}"

class Jangchi(Qahramon):
    def __init__(self, nomi):
        super().__init__(nomi, salomatlik=100, hujum=30)
        self.qalqon = True
    
    def hujum_qilish(self):  # Polimorfizm
        asosiy_zarar = super().hujum_qilish()
        return int(asosiy_zarar * 1.2)  # Jangchi 20% kuchliroq
    
    def maxsus_hujum(self):
        return "⚔️ Qilich bilan kuchli hujum!"

class Sehrgar(Qahramon):
    def __init__(self, nomi):
        super().__init__(nomi, salomatlik=80, hujum=40)
        self.mana = 100
    
    def hujum_qilish(self):  # Polimorfizm
        if self.mana >= 20:
            self.mana -= 20
            return random.randint(self.hujum - 10, self.hujum + 10)
        else:
            return super().hujum_qilish()  # Oddiy hujum
    
    def sehr_qilish(self):
        if self.mana >= 50:
            self.mana -= 50
            return "🔮 Kuchli sehr hujumi!"
        return "Mana yetarli emas!"

class Kamanda(Qahramon):
    def __init__(self, nomi):
        super().__init__(nomi, salomatlik=90, hujum=35)
        self.oqlar_soni = 3
    
    def hujum_qilish(self):  # Polimorfizm
        if self.oqlar_soni > 0:
            self.oqlar_soni -= 1
            return self.hujum + 15  # O'q bilan kuchliroq
        return super().hujum_qilish()
    
    def oqlarni_qayta_yuklash(self):
        self.oqlar_soni = 3
        return "🎯 O'qlar qayta yuklandi!"

# O'yin jarayoni
def jang_qilish(qahramon1, qahramon2):
    print(f"🎮 JANG BOSHLANDI: {qahramon1.nomi} vs {qahramon2.nomi}")
    print("=" * 40)
    
    raund = 1
    while qahramon1.tirikmi() and qahramon2.tirikmi():
        print(f"Raund {raund}:")
        
        # Qahramon1 hujum qiladi
        zarar1 = qahramon1.hujum_qilish()
        qahramon2.zarar_olish(zarar1)
        print(f"{qahramon1.nomi} hujum qildi: {zarar1} zarar")
        
        if not qahramon2.tirikmi():
            print(f"🎉 {qahramon1.nomi} g'alaba qozondi!")
            break
        
        # Qahramon2 hujum qiladi
        zarar2 = qahramon2.hujum_qilish()
        qahramon1.zarar_olish(zarar2)
        print(f"{qahramon2.nomi} hujum qildi: {zarar2} zarar")
        
        print(f"Holat: {qahramon1.holatni_korsat()} | {qahramon2.holatni_korsat()}")
        print("-" * 30)
        raund += 1
    
    if qahramon2.tirikmi():
        print(f"🎉 {qahramon2.nomi} g'alaba qozondi!")

# Test qilamiz
jangchi = Jangchi("Qahramon")
sehrgar = Sehrgar("Sehrgar")
kamanda = Kamanda("Nishonchi")

jang_qilish(sehrgar, kamanda)