# 14 - Dars | Funksiyalar (Kodni qayta ishlatish va tashkil qilish)


# Oddiy funksiya yaratish
def salom_ber():
    """salomlashuvchi funksiya"""
    print("Assalomu alaykum!")
    print("Python o'rganishga xush kelibsiz!")

salom_ber()
print(range.__doc__)



##
# # Parametrli funksiya
def salom_ber(ism):
    print(f"Assalomu alaykum, {ism}!")

# Argument bilan chaqirish
salom_ber("Ali")
salom_ber("Vali")


###
# Return bilan funksiya
def kvadrat_top(son):
    kvadrat = son * son
    return kvadrat

Funksiyani chaqirib, natijani saqlash
natija = kvadrat_top(5)
print(f"5 ning kvadrati: {natija}")

# To'g'ridan-to'g'ri chiqarish
print(f"7 ning kvadrati: {kvadrat_top(7)}")


####
# Bir nechta parametrlar
def toplayish(a, b):
    return a + b

def kopaytirish(a, b):
    return a * b

# # # Funksiyalarni chaqirish
print(f"5 + 3 = {toplayish(5, 3)}")
print(f"4 * 6 = {kopaytirish(4, 6)}")

Turli ma'lumot turlari
def ishchi_maoshi(ism, soat, stavka):
    maosh = soat * stavka
    return f"{ism}ning maoshi: {maosh} so'm"

print(ishchi_maoshi("Ali", 40, 25000))


#####
# Standart parametr qiymatlari
def salom_ber(ism="Mehmon"):
    print(f"Salom, {ism}!")

# Argument bermasak, standart qiymat ishlatiladi
# salom_ber()          # Salom, Mehmon!
salom_ber("Ali")     # Salom, Ali!

Bir nechta standart parametrlar
def hisobla(a, b=1, c=1):
    return a * b * c

print(hisobla(5))    # 5 * 1 * 1 = 5
print(hisobla(5, 2))     # 5 * 2 * 1 = 10
print(hisobla(5, 2, 3))  # 5 * 2 * 3 = 30



######
# Matematik funksiyalar
def qoshish(a, b):
    return a + b

def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b

def bolish(a, b):
    if b != 0:
        return a / b
    else:
        return "Nolga bo'lish mumkin emas!"

# Kalkulyator dasturi
print("Kalkulyator dasturiga xush kelibsiz! 🧮")
print("Mavjud amallar: +, -, *, /")

a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))
amal = input("Amalni tanlang (+, -, *, /): ")

if amal == "+":
    natija = qoshish(a, b)
elif amal == "-":
    natija = ayirish(a, b)
elif amal == "*":
    natija = kopaytirish(a, b)
elif amal == "/":
    natija = bolish(a, b)
else:
    natija = "Noto'g'ri amal!"

print(f"Natija: {natija}")