# 18 - Dars | OOP Asoslari (Class va Object bilan tanishuv)

class Mashina:
    def __init__(self, model, rang, yil,):
        self.model = model
        self.rang = rang
        self.yil = yil
        self.yurgan_masofa = 0

    def malumo_ber(self):
        return f"{self.model} {self.rang} {self.yil} - Yil"
    
    def haydash(self, km):
        self.yurgan_masofa += km
        return f"{km} km yo'l yurildi. Jami: {self.yurgan_masofa} km"
    
    def signal_ber(self):
        return f"{self.model} signal berdi: BEEP BEEP"



malibu = Mashina("Malibu", "qora", 2020)
print(malibu.malumo_ber())
print(malibu.haydash(60))
print(malibu.signal_ber())





Class - shablon (reja)
class Talaba:
    universitet = "Termiz davlat muhandislik va agrotexnologiyalar universiteti"
    
    def __init__(self, ism, yosh, fakultet):
        self.ism = ism
        self.yosh = yosh
        self.fakultet = fakultet 
    
    def tanishtir(self):
        return f"Men {self.ism}, {self.fakultet} fakultetida o'qiyman"

# Objectlar - haqiqiy talabalar
talaba1 = Talaba("Ali", 20, "Dasturlash")
talaba2 = Talaba("Vali", 21, "Matematika")
talaba3 = Talaba("Hasan", 19, "Fizika")

print(talaba1.tanishtir())
print(talaba2.tanishtir())
print(talaba3.tanishtir())

print(f"Hammamiz {Talaba.universitet} da o'qiymiz!")



##
class BankHisob:
    def __init__(self, ism, balans=0):
        self.ism = ism
        self.balans = balans
        print(f"Yangi hisob ochildi: {self.ism}")
    
    def depozit(self, miqdor):
        # self.balans - joriy hisobning balansi
        self.balans += miqdor
        return f"{miqdor} so'm qo'shildi. Yangi balans: {self.balans}"
    
    def yechish(self, miqdor):
        if miqdor <= self.balans:
            self.balans -= miqdor
            return f"{miqdor} so'm yechildi. Yangi balans: {self.balans}"
        else:
            return "Balansda yetarli mablag' yo'q!"
    
    def balansni_korsat(self):
        return f"{self.ism} ning balansi: {self.balans} so'm"

# Ikki xil hisob ochamiz
ali_hisob = BankHisob("Ali", 1000)
vali_hisob = BankHisob("Vali", 500)

print(ali_hisob.depozit(300))
print(vali_hisob.depozit(200))
print(ali_hisob.balansni_korsat())  
print(vali_hisob.balansni_korsat()) 



### AMALIY LOYIHA
class AqlliTelefon:
    def __init__(self, model, ishlab_chiqaruvchi, xotira):
        self.model = model
        self.ishlab_chiqaruvchi = ishlab_chiqaruvchi
        self.xotira = xotira  # GB da
        self.qolgan_xotira = xotira
        self.ilovalar = []
        self.qong_iroq = False
    
    def telefon_haqida(self):
        return f"{self.model} ({self.ishlab_chiqaruvchi}) - {self.xotira}GB"
    
    def ilova_yuklab_olish(self, ilova_nomi, hajmi):
        if hajmi <= self.qolgan_xotira:
            self.ilovalar.append(ilova_nomi)
            self.qolgan_xotira -= hajmi
            return f"✅ {ilova_nomi} yuklab olindi! Qolgan xotira: {self.qolgan_xotira}GB"
        else:
            return f"❌ Xotira yetarli emas! Kerak: {hajmi}GB, Mavjud: {self.qolgan_xotira}GB"
    
    def ilovalarni_korsat(self):
        if not self.ilovalar:
            return "📱 Ilovalar yo'q"
        
        ilovalar_listi = "📱 Yuklangan ilovalar:\n"
        for ilova in self.ilovalar:
            ilovalar_listi += f"  • {ilova}\n"
        return ilovalar_listi
    
    def qong_iroqni_ochish(self):
        self.qong_iroq = False
        return "🔦 Qo'ng'iroq ochildi!"
    
    def qong_iroqni_yopish(self):
        self.qongiroq = True
        return "🔦 Qo'ng'iroq yopildi!"
    
    def qong_iroq_holati(self):
        return "🔦 Yoniq" if self.qong_iroq else "🔦 O'chiq"

# Telefon yaratamiz
iphone = AqlliTelefon("iPhone 15", "Apple", 128)
samsung = AqlliTelefon("Galaxy S23", "Samsung", 256)

# print(iphone.telefon_haqida())
# print(samsung.telefon_haqida())

print(iphone.ilova_yuklab_olish("Instagram", 0.5))
print(iphone.ilova_yuklab_olish("Telegram", 0.3))
print(iphone.ilova_yuklab_olish("YouTube", 2.0))

print(iphone.ilovalarni_korsat())
print(iphone.qong_iroqni_yopish())
print(iphone.qong_iroq_holati())