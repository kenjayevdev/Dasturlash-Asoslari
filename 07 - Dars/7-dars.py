# 07 - Dars | Python Operatorlari (Arifmetik, Taqqoslash, Mantiqiy)


# 1-ARIFMETIK OPERATORLAR
#qo'shish
a = 10 + 5
print("10 + 5 =", a)

#Ayrish
b = 20 - 15
print("20 - 15 =", b)

#ko'paytirish
c = 10 * 5
print("10 * 5 =", c)

#bo'lish
d = 10 / 3
print("10 / 3 =", d)

#butun qisimga bo'lish
e = 10 // 3
print("10 // 3 =", e)

#qoldiq olish
f = 10 % 3
print("10 % 3 =", f)

#darajaga oshirish
g = 2 ** 3
print("2 ** 3 =", g)

# 2-TAQQOSLASH OPERATORLAR

x = 10
y = 5

#Tenglik (==)
print("x == y:", x == y)

#Teng emas (!=)
print("x != y:", x != y)

#Katta (>)
print("x > y:", x > y)

#Kichik (<)
print("x < y:", x < y)

#Kichik yoki teng (<=)
print("x <= y:", x <= y)

# 3-MANTIQIY OPERATORLAR

a = True
b = False

# AND operatori (va)
print("a AND b:", a and b)

# OR operatori (yoki)
print("a OR b:", a or b)

# NOT operatori (emas)
print("NOT a:", not a)


yosh = int(input("Yoshingiz Nechida? "))

min_yosh = 18
max_yosh = 65

if yosh >= min_yosh and yosh <= max_yosh:
    print("Xush kelibsiz kirishingiz mumkin.")
else:
    print("Kechirasiz, kirish mumkin emas.")