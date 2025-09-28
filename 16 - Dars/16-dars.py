# 16 - Dars | Fayllar bilan ishlash (Ma'lumotlarni Saqlash va O'qish)



# Fayl yaratish va yozish
fayl = open("test.txt", "w")  # "w" - yozish uchun ochish
fayl.write("Salom, Python!\n")
fayl.write("Bu birinchi faylimiz.\nuchunchi matinimiz")
fayl.close()  # Faylni yopish

# Fayldan o'qish
fayl = open("test.txt", "r")  # "r" - o'qish uchun ochish
matn = fayl.read()
print(matn)
fayl.close()


##
# With operatori bilan fayl ishlash
with open("test.txt", "w") as fayl:
    fayl.write("Salom, Python!\n")
    fayl.write("With operatori juda qulay!\n")

# Fayl avtomatik yopiladi

# O'qish ham with bilan
with open("test.txt", "r") as fayl:
    matn = fayl.read()
    print(matn)
    
    


###
with open("maqola.txt", "w") as f:
    f.write("Birinch qator\n")
    f.write("Ikkinchi qator\n")
    f.write("Uchinchi qator\n")

# 1. read() - barchasini o'qish
with open("maqola.txt", "r") as f:
    print("read() metodi:")
    print(f.read())

# 2. readline() - bir qator o'qish
with open("maqola.txt", "r") as f:
    print("\nreadline() metodi:")
    print(f.readline())  # Birinchi qator


# 3. readlines() - barcha qatorlarni ro'yxatda o'qish
with open("maqola.txt", "r") as f:
    print("\nreadlines() metodi:")
    qatorlar = f.readlines()
    for qator in qatorlar:
        print(qator.strip())  # strip() - bo'shliqlarni olib tashlaydi


####
import json

# Ma'lumotlarni JSON fayliga saqlash
talaba = {
    "ism": "Ali",
    "yosh": 20,
    "kurs": 3,
    "fakultet": "Dasturlash",
    "baholar": [85, 90, 78, 92]
}

with open("talaba.json", "w") as f:
    json.dump(talaba, f, indent=4)  # indent=4 - chiroyli ko'rinish

# # JSON fayldan o'qish
with open("talaba.json", "r") as f:
    malumot = json.load(f)
    print("JSON fayldan o'qilgan ma'lumot:")
    print(f"Ism: {malumot['ism']}")
    print(f"Yosh: {malumot['yosh']}")
    print(f"Baholar: {malumot['baholar']}")
   


##### AMALIY LOYIHA
import datetime

def kundalik_yoz():
    """Yangi kundalik yozish"""
    sana = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = input("Bugun nima qildingiz? ")
    
    with open("kundalik.txt", "a", encoding="utf-8") as f:
        f.write(f"{sana}: {entry}\n")
    print("Kundalik saqlandi! ✅")

def kundalik_oqish():
    """Kundalikni o'qish"""
    try:
        with open("kundalik.txt", "r", encoding="utf-8") as f:
            print("\n📖 Sizning kundaligingiz:")
            print("=" * 40)
            print(f.read())
    except FileNotFoundError:
        print("Hali kundalikingiz yo'q. Birorta yozing!")

# Asosiy dastur
while True:
    print("\n📓 Shaxsiy Kundalik Dasturi")
    print("1. Yangi kundalik yozish")
    print("2. Kundalikni o'qish")
    print("3. Chiqish")
    
    tanlov = input("Tanlovingiz (1-3): ")
    
    if tanlov == "1":
        kundalik_yoz()
    elif tanlov == "2":
        kundalik_oqish()
    elif tanlov == "3":
        print("Dasturdan chiqildi. Xayr! 👋")
        break
    else:
        print("Noto'g'ri tanlov! Iltimos, 1-3 oralig'ida tanlang.")