# 06 - Dars | Matnlar bilan ishlash (String Methods & Formatting)

matin = " Python dasturlash tili "

print(matin.upper())

print(matin.lower())

print(matin.strip())

print(matin.replace("Python", "python"))

print(matin.split())

#f-string 1-usuli
ism = "aziz"
yosh = 23
kasbi = "dasturchi"

# #f-string usuli
xabar = f"Mening ismim {ism}. Men {yosh} yoshdaman. kasbim - {kasbi}"
print(xabar)

#format() 2-usul
ism = "aziz"
yosh = 23
kasbi = "dasturchi"
familiya = "xurammov"
xabar = "Mening ismim {}. Mening familiyam {} Men {} yoshdaman. Kasbim - {}.".format(ism,  familiya, yosh, kasbi)
print(xabar)

#string indekslari va kesish

matn = "Python"

print(matn[0])
print(matn[1])
print(matn[2])
print(matn[3])
print(matn[4])
print(matn[5])

print(matn[-1])
print(matn[-2])

matn = "Dsturlash"

print(matn[0:5])
print(matn[10:5])
print(matn[:5])
print(matn[::2])
print(matn[::-1])

ism = "Aziz"
familiya = "yuldashev"
toliq_ism = ism + " " + familiya
print(toliq_ism)

border = "-" * 50
print(border)

matn = "Python"
print(len(matn))

matn = "Python"
print("P" in matn)
print("z" in matn)

print("salom\ndunyo")
print("Ism:\tAli")
print("U \"Python\"ni yaxshi koradi")

#1-amaliy
ism = input("Ismingiz nima? ")

xabar = f"Salom, {ism.title()}! Pythoni o'rganishga xush kelibsiz"

print(xabar)

#2-Amaliy 
matn = "  python DASTURLASH tili juda ajoyib  "

tartibli_matin = matn.strip().lower().capitalize()
print(tartibli_matin)

sozlar = tartibli_matin.split()
print(f"Matinda {len(sozlar)} ta so'z bor")
