# 09 - Dars | Lug'atlar (Dictionaries) kalit-qiymat asosida ma'lumot saqlash


# Oddiy lug'at yaratish
talaba = {
    "ism": "Ali",
    "yosh": 20,
    "kurs": 3,
    "fakultet": "Dasturlash"
}

print(talaba)


talaba = {
    "ism": "Aziza",
    "yosh": 21,
    "kurs": 2,
    "fakultet": "Matematika",
    "yo'nalish": "fizika"
}


print(talaba["ism"]) 
print(talaba["yosh"])


print(talaba.get("kurs"))    # 2
print(talaba.get("baholari", "Ma'lumot topilmadi"))

##
talaba = {"ism": "Sardor", "yosh": 19}

talaba["kurs"] = 1
talaba["fakultet"] = "Fizika"
talaba["shahri"] = "Termiz Shahar"

print(talaba)

talaba["yosh"] = 20
talaba["kurs"] = 2

print(talaba)


###
talaba = {
    "ism": "Nigora",
    "yosh": 22,
    "kurs": 4,
    "fakultet": "Kimyo"
}

print(talaba.keys())

print(talaba.values())

print(talaba.items())


####

talaba = {
    "ism": "Javohir",
    "yosh": 23,
    "kurs": 5,
    "fakultet": "Biologiya"
}

yosh = talaba.pop("yosh")
print(yosh)
print(talaba)

element = talaba.popitem()
print(element)
print(talaba)

del talaba["kurs"]
print(talaba)

talaba.clear()
print(talaba)

#####
talaba = {
    "ism": "Farida",
    "yosh": 24,
    "kurs": 6,
    "fakultet": "Tarix"
}

for kalit in talaba:
    print(kalit)

for kalit, qiymat in talaba.items():
    print(f"{kalit}: {qiymat}")


##AMALIY

telefon_kitob = {}

while True:
    print("\nTelefon Kitobi")
    print("1. Kontakt qo'shish")
    print("2. Kontakt ko'rish")
    print("3. Kontakt o'chirish")
    print("4. Chiqish")
    
    tanlov = input("Tanlovingiz: ")
    
    if tanlov == "1":
        ism = input("Ism: ")
        telefon = input("Telefon: ")
        telefon_kitob[ism] = telefon
        print(f"{ism} qo'shildi!")
        
    elif tanlov == "2":
        if telefon_kitob:
            print("\nKontaktlar:")
            for ism, telefon in telefon_kitob.items():
                print(f"{ism}: {telefon}")
        else:
            print("Telefon kitobi bo'sh!")
            
    elif tanlov == "3":
        ism = input("O'chiriladigan kontakt ismi: ")
        if ism in telefon_kitob:
            telefon_kitob.pop(ism)
            print(f"{ism} o'chirildi!")
        else:
            print("Bunday kontakt topilmadi!")
            
    elif tanlov == "4":
        print("Dasturdan chiqildi!")
        break
        
    else:
        print("Noto'g'ri tanlov!")
