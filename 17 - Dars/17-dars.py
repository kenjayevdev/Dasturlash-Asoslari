# 17 - Dars | Xatolarni Boshqarish (Try, Except, Finally)



# Xato kelib chiqadigan misol
try:
    son = int(input("Son kiriting: ")) 
    natija = 10 / son                
    print(f"Natija: {natija}")
except:
    print("faqat butun son kiritish mumkin va 0 dan katta son kiritish mumkin")


##
try:
    son = int(input("Son kiriting: "))
    natija = 10 / son
    print(f"Natija: {natija}")
    
except ValueError:
    # Raqam emas matn kiritilganda
    print("Iltimos, raqam kiriting! Matn kiritdingiz.")
    
except ZeroDivisionError:
    # Nolga bo'lishga urinilganda
    print("Nolga bo'lish mumkin emas! Boshqa son kiriting.")
    
except Exception as x:
    # Boshqa barcha xatolar
    print(f"Kutilmagan xato: {x}")
    
    
    
# ####
try:
    son = int(input("Son kiriting: "))
    natija = 10 / son
    
except ValueError:
    print("Iltimos, raqam kiriting!")
    
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas!")
    
else:
    # Xato bo'lmasa bajariladi
    print(f"Muammosiz hisoblandi! Natija: {natija}")
    
finally:
    # Har doim bajariladi
    print("Dastur yakunlandi.")
    
    

# #####
def yosh_tekshir(yosh):
    if yosh < 0:
        raise ValueError("Yosh manfiy bo'lishi mumkin emas!")
    elif yosh > 150:
        raise ValueError("Yosh 150 dan katta bo'lishi mumkin emas!")
    else:
        return f"Yoshingiz: {yosh}"

try:
    print(yosh_tekshir(25))   # Normal
 
    print(yosh_tekshir(200))  # Xato
    
except ValueError as x:
    print(f"Xato: {x}")
    
    
# ######
try:
    son = int(input("Son kiriting: "))
    natija = 10 / son
    print(f"Natija: {natija}")
    
except (ValueError, ZeroDivisionError) as x:
    print(f"Xato turi: {type(x).__name__}")
    print(f"Xato xabari: {x}")
    
    if isinstance(x, ValueError):
        print("Siz noto'g'ri qiymat kiritdingiz.")
    elif isinstance(x, ZeroDivisionError):
        print("Siz nolga bo'lishga urindingiz.")
        
        
 
 
 #AMALIY LOYIHA
import os

def fayl_tekshiruvchi():
    """Fayl operatsiyalarida xatolarni boshqarish"""
    
    while True:
        print("\n📁 Fayl Tekshiruvchi")
        print("1. Fayl yaratish va yozish")
        print("2. Fayldan o'qish")
        print("3. Fayl mavjudligini tekshirish")
        print("4. Chiqish")
        
        try:
            tanlov = input("Tanlovingiz (1-4): ")
            
            if tanlov == "4":
                break
                
            if tanlov == "1":
                fayl_nomi = input("Fayl nomi: ")
                matn = input("Yoziladigan matn: ")
                
                with open(fayl_nomi, "w", encoding="utf-8") as f:
                    f.write(matn)
                print(f"'{fayl_nomi}' fayliga yozildi! ✅")
                
            elif tanlov == "2":
                fayl_nomi = input("Fayl nomi: ")
                
                if not os.path.exists(fayl_nomi):
                    raise FileNotFoundError(f"'{fayl_nomi}' fayli topilmadi!")
                
                with open(fayl_nomi, "r", encoding="utf-8") as f:
                    print(f"Fayl tarkibi:\n{f.read()}")
                    
            elif tanlov == "3":
                fayl_nomi = input("Fayl nomi: ")
                
                if os.path.exists(fayl_nomi):
                    print(f"'{fayl_nomi}' fayli mavjud! ✅")
                else:
                    print(f"'{fayl_nomi}' fayli mavjud emas! ❌")
                    
            else:
                raise ValueError("Noto'g'ri tanlov!")
                
        except FileNotFoundError as x:
            print(f"Fayl xatosi: {x}")
            print("Iltimos, fayl nomini to'g'ri kiriting.")
            
        except PermissionError:
            print("Faylga yozish huquqi yo'q!")
            
        except ValueError as x:
            print(f"Qiymat xatosi: {x}")
            
        except Exception as x:
            print(f"Kutilmagan xato: {x}")
            
        finally:
            print("-" * 40)

# Dasturni ishga tushirish
fayl_tekshiruvchi()