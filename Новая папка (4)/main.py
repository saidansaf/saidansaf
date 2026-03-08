def kopaytma(*args):
    result = 1
    for son in args:
        result *= son
    print("1. Sonlarning ko'paytmasi:", result)

def foydalanuvchi(**kwargs):
    print("\n2. Foydalanuvchi ma'lumotlari:")
    for kalit, qiymat in kwargs.items():
        print(kalit, ":", qiymat)

def matn_uzunligi(*args):
    print("\n3. Matnlarning uzunligi:")
    for matn in args:
        print(matn, "->", len(matn))

def musbat_sonlar(*args):
    musbat = []
    for son in args:
        if son > 0:
            musbat.append(son)
    print("\n4. Musbat sonlar:", musbat)

def toliq_malumot(*args, **kwargs):
    print("\n5. Qo'shimcha ma'lumotlar:")
    
    print("Qiziqishlar:")
    for qiziqish in args:
        print("-", qiziqish)
    
    print("Asosiy ma'lumotlar:")
    for kalit, qiymat in kwargs.items():
        print(kalit, ":", qiymat)

kopaytma(2, 3, 4)
foydalanuvchi(ism="Ali", yosh=20, kasb="Dasturchi")
matn_uzunligi("salom", "python", "dasturlash")
musbat_sonlar(-3, 5, -1, 7, 0, 9)
toliq_malumot("Futbol", "Kitob o'qish", ism="Ali", yosh=20, kasb="Dasturchi")