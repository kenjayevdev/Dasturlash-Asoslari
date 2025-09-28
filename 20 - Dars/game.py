# 20 - Dars | Yakuniy Loyiha (Tasodifiy raqam o‘yinini yasaymiz)


import tkinter as tk
import random

sirli_son = random.randint(1, 100)
urinish = 0

def taxmin_tekshir():
    global urinish
    taxmin = kiritish.get()

    if not taxmin.isdigit():
        natija_yozuvi.config(text="Iltimos, faqat raqam kiriting!", fg="red")
        return
    
    taxmin = int(taxmin)
    urinish += 1

    if taxmin < sirli_son:
        natija_yozuvi.config(text="⬆️ Kattaroq son kiriting", fg="orange")
        kiritish.delete(0, tk.END)
    elif taxmin > sirli_son:
        natija_yozuvi.config(text="⬇️ Kichikroq son kiriting", fg="blue")
        kiritish.delete(0, tk.END)
    else:
        natija_yozuvi.config(text=f"🎉 To'g'ri! Siz {urinish} urinishda topdingiz!", fg="green")

        kiritish.config(state="disabled")

        taxmin_tugmasi.config(state="disabled")

def qayta_boshlash():
    global sirli_son, urinish
    sirli_son = random.randint(1, 100)
    urinish = 0
    kiritish.config(state="normal")
    taxmin_tugmasi.config(state="normal")
    kiritish.delete(0, tk.END)
    natija_yozuvi.config(text="Yangi o'yin boshlang!", fg="#333")
                         
# Tkinter asosiy oyna hosil qilish
oyna = tk.Tk()
oyna.title("🎲 Sonni Top O'yni")
oyna.geometry("400x400")
oyna.configure(bg="#E6F2FF")

# Sarlavha

sarlqvha = tk.Label(
    oyna,
    text="1 dan 100 gacha son o'yladim.\nTopa olasizmi?",
    font=("Helvetic", 16, "bold"),
    bg="#E6F2FF",
    fg="#004080"

)
sarlqvha.pack(pady=20)

#son kiritish maydoni
kiritish = tk.Entry(
    oyna,
    font=("Arial",14),
    justify=("center"),
    bg="#F0F9FF",
    fg="#003366",
    width=10

)
kiritish.pack(pady=10)

taxmin_tugmasi = tk.Button(
    oyna,
    text="✅ Taxmin qilish",
    font=("Arial", 12, "bold"),
    bg="#66CCFF",
    fg="white",
    command=taxmin_tekshir

)
taxmin_tugmasi.pack(pady=10)
#natija yozuvi
natija_yozuvi = tk.Label(
    oyna,
    text="",
    font=("Arial", 14),
    bg="#E6F2FF",
    fg="#333"
)
natija_yozuvi.pack(pady=20)

#qayta boshlash
qayta_boshlash = tk.Button(
    oyna,
    text="🔄 Qayta o'ynash",
    font=("Arial", 10, "bold"),
    bg="#99CC33",
    fg="white",
    command=qayta_boshlash
)
qayta_boshlash.pack(pady=10)
oyna.mainloop()