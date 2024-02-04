"""
            04.02.2024 1-dars
            son topish o'yini
            tuzuvchi: Zokirov Bahodir
"""

oraliq = int (input ("Keling bir o'yin o'ynamiz!\nO'yinimiz sharti:"
       " men son o'ylayman siz topishingiz kerak bo'ladi, "
       "keyin siz son o'ylaysiz men topaman"
       "\noraliqni tanlang:"
       "\n>>> 1. 0 dan 10 gacha\n>>> 2. 0 dan 100 gacha\n>>> 3. 0 dan 1000 gacha\nKiriting: "))

if oraliq == 1:
    b = 10
elif oraliq == 2:
    b = 100
elif oraliq == 3:
    b = 1000

import random as r

# print (son)

oynaymizmi = "yes"


while oynaymizmi == "yes":
    son = r.randint(0, b=b)

    men = 0
    kompyuter = 0
    mening_sonim = int(input("Men son o'yladim topishga harakat qiling: "))

    while True:
        men += 1
        if mening_sonim > son:
            mening_sonim = int (input (f"Men o'ylagan son {mening_sonim} dan kichik: Qayta urinib ko'ring\n>>> "))
        elif mening_sonim < son:
            mening_sonim = int (input (f"Men o'ylagan son {mening_sonim} dan katta. Qayta urinib ko'ring\n>>> "))
        elif mening_sonim == son:
            print (f"Tabriklayman, topdingiz men o'ylagan son {son} edi.\n")
            # print (f"siz {men} ta urinishda topdingiz.\n\n ")
            break


    min_son = 0
    max_son = b


    print ("Endi siz son o'ylang men topaman")
    siz_oylagan_son = r.randint(1, b)
    while True:
        kompyuter += 1

        print (f"Siz o'ylagan son: {siz_oylagan_son} mi?!")
        res = input (f"Men o'ylagan son: \n>>> a. {siz_oylagan_son} dan kichik \n>>> b. {siz_oylagan_son} dan katta \n>>> c. Topding, bu son {siz_oylagan_son} edi.\n>>> ")
        if res == "a":
            max_son = siz_oylagan_son
        elif res == "b":
            min_son = siz_oylagan_son
        elif res == "c":
            print (f"Topding men o'ylagan son {siz_oylagan_son} edi. \n")
            break


        siz_oylagan_son = r.randint (min_son + 1, max_son - 1)

    if kompyuter > men:
        print (f"Hisob, Siz: {men}, Men: {kompyuter}\nSiz yutdingiz")
    elif kompyuter < men:
        print(f"Hisob, Siz: {men}, Men: {kompyuter}\nMen yutdim")
    else:
        print(f"Hisob, Siz: {men}, Men: {kompyuter}\nDurrang")

    oynaymizmi = input ("Yana o'ynaymizmi: Davom ettirish uchun 'yes' ni, tugatish uchun 'no' ni kiriting\n>>> ")


else:
    print ("\nO'yin ajoyib bo'ldi chiroyli o'yin uchun raxmat")