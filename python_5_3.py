#اسم بگیرد و اگر در لیست بود ایندکس اون اسم رو به عنوان خروجی چاپ کند
hamclassi=["reza","ali","sara","mahdi","mina"]
name=input("esmet chie?\n")
if name in hamclassi:
    for index,name in enumerate(hamclassi):
        print(index)

else:
    print("esm shoma dar list nist")
