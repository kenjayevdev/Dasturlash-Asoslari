# 05 - Dars | Ma'lumot Turlari Bilan Tanishish (Data Types in Python)

#1 Integer - butun sonlar (10, -5, 0)
#2 Float - o'nlik sonlar (2.14, -0.5, 2.0)
#3 String - matinlar ("salom","python","12")
#4 Boolean - Mantiqiy qiymatlar (True, False)

# 1 Integer
yosh = 25
talabalar_soni = 30
print(yosh)
print(talabalar_soni)

# 2 Float
pi = 3.14
ogirlik = 55.5
harorat = 25.7
print(pi)
print(ogirlik)

# 3 String
ism = "ali"
familya = "Valiyev"
shahar = "Toshkent"

print(ism)
print(familya)
print(shahar)

toliq_ism = ism + " " + familya
print(toliq_ism)

# 4 Boolean
yomgir_yogayabdi = False
kun_yorug = True

print(yomgir_yogayabdi)
print(kun_yorug)

# type()
print(type(10))
print(type(3.14))
print(type("salom"))
print(type(True))

yosh = 25
print(type(yosh))

ism = "Anvar"
print(type(ism))

int() - butun songa o'zgartirish
float() - o'nlik songa o'zgartirish
str() - matinga o'zgartirish
bool() - mantiqiy qiymatga o'zgartirish

n = "123"
print(type(n))
n = int(n)
print(type(n))


yosh = 25
print(type(yosh))
yosh_matn = str(yosh)
print(type(yosh_matn))
print("Mening yoshim" + yosh_matn)

# Amaliy mashiq

yosh = 25
print("Mening yoshim" + str(yosh))

















